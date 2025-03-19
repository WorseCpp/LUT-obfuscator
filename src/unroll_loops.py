from qol import *

def add_goto_delete_while(fxn):

    # Create a unique label name
    label_name = rand_name()

    for i, stmt in enumerate(fxn.body.block_items):
        if isinstance(stmt, c_ast.While):

            # Create the label node
            label = c_ast.Label(name=label_name, stmt=c_ast.Compound(block_items=[]))

            # Create the goto statement node
            goto_stmt = c_ast.Goto(name=label_name)

            # Add the label at the position of the while loop
            fxn.body.block_items[i] = label

            # Add the while loop body to the label's block items
            label.stmt.block_items.extend(stmt.stmt.block_items)

            # Add the condition check and goto statement at the end of the label's block items
            label.stmt.block_items.append(c_ast.If(
                cond=stmt.cond,
                iftrue=goto_stmt,
                iffalse=None
            ))

            return fxn, label_name, True
    return fxn, label_name, False

def unroll_all_while(fxn):
    fxn, label_name, changed = add_goto_delete_while(fxn)
    while changed:
        fxn, label_name, changed = add_goto_delete_while(fxn)
    return fxn

def add_goto_delete_for(fxn):

    # Create a unique label name
    label_name = rand_name()
    end_label_name = rand_name()
    for i, stmt in enumerate(fxn.body.block_items):
        if isinstance(stmt, c_ast.For):
            # If an initialization exists, insert it before the loop
            if stmt.init is not None:
                for decl in stmt.init:
                    fxn.body.block_items.insert(i, decl)
                    i += 1  # adjust index after insertion
            # Create the label node
            label = c_ast.Label(name=label_name, stmt=c_ast.Compound(block_items=[]))
            end_label = c_ast.Label(name = end_label_name, stmt = c_ast.Compound(block_items=[]))
            
            # Replace the for loop with the label
            fxn.body.block_items[i] = label

            fxn.body.block_items.insert(i+1, c_ast.If(
                    cond=stmt.cond,
                    iftrue=c_ast.Compound(block_items=[]),
                    iffalse=c_ast.Compound(block_items=[c_ast.Goto(name=end_label_name)])
                ))
            
            i += 1

            # Add the loop's body; wrap non-compound bodies in a compound statement
            if isinstance(stmt.stmt, c_ast.Compound):
                for loop_operation in stmt.stmt.block_items +[stmt.next]:
                    fxn.body.block_items.insert(i+1, loop_operation)
                    i += 1
            else:
                fxn.body.block_items.insert(i, stmt.stmt)

            # Add the condition check: if (cond) goto label; if no condition, do an unconditional goto
            if stmt.cond is not None:
                fxn.body.block_items.insert(i+1, c_ast.Goto(name=label_name))
                i += 1

            else:
                fxn.body.block_items.insert(i+1, c_ast.Goto(name=label_name))
                i += 1

            fxn.body.block_items.insert(i+1, end_label)
            return fxn, label_name, True
    
    return fxn, label_name, False


def unroll_all_for(fxn):
    fxn, label_name, changed = add_goto_delete_for(fxn)
    while changed:
        fxn, label_name, changed = add_goto_delete_for(fxn)
    return fxn

def unroll_loops(fxn):
    fxn = unroll_all_while(fxn)
    fxn = unroll_all_for(fxn)
    return fxn