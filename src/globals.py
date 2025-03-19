from qol import *

def globalize_local(ast):
    # Get all function definitions from the top-level declarations.
    func_defs = [node for node in ast.ext if isinstance(node, c_ast.FuncDef)]
    if not func_defs:
        return ast

    # Pick a random function.
    selected_func = random.choice(func_defs)
    # If the function has no body or no block items, nothing to do.
    if not selected_func.body or not selected_func.body.block_items:
        return ast

    # Find all local variable declarations directly in the function's block.
    local_decls = [stmt for stmt in selected_func.body.block_items if isinstance(stmt, c_ast.Decl)]
    if not local_decls:
        return ast

    # Pick a random local declaration.
    selected_decl = random.choice(local_decls)
    # Replace the local variable declaration with an assignment statement.
    index = selected_func.body.block_items.index(selected_decl)
    init_value = selected_decl.init if selected_decl.init is not None else c_ast.Constant(type="int", value="0")
    assignment = c_ast.Assignment(op="=", lvalue=c_ast.ID(name=selected_decl.name), rvalue=init_value)
    selected_func.body.block_items[index] = assignment
    # Add the variable declaration as a global declaration.
    
    decl = c_ast.Decl(name=selected_decl.name,
                      quals=selected_decl.quals,
                      storage=selected_decl.storage,
                      funcspec=selected_decl.funcspec,
                      type=selected_decl.type,
                      init=None,
                      bitsize=selected_decl.bitsize,
                      align=None)

    ast.ext.insert(0, decl)
    
    return ast

def delete_global(ast):
    # Collect global variable declarations (exclude function definitions)
    global_decls = [node for node in ast.ext if isinstance(node, c_ast.Decl) and not isinstance(node.type, c_ast.FuncDecl)]
    if len(global_decls) < 2:
        # Need at least two globals to perform replacement
        return ast

    # Randomly select a global variable to delete
    candidate = random.choice(global_decls)

    # Use c_generator to get a string representation of its type
    gen = c_generator.CGenerator()
    candidate_type_str = gen.visit(candidate.type)

    # Find replacement globals with the same type (excluding the candidate)
    same_type_globals = [node for node in global_decls if node is not candidate and gen.visit(node.type) == candidate_type_str]
    if not same_type_globals:
        # No replacement found; do nothing
        return ast

    # Randomly choose a replacement global variable of the same type
    replacement = random.choice(same_type_globals)
    candidate_name = candidate.name
    replacement_name = replacement.name

    # Remove the candidate from the list of top-level declarations
    ast.ext.remove(candidate)

    # Traverse the AST and replace all references of candidate with replacement
    class GlobalVarReplacer(c_ast.NodeVisitor):
        def visit_ID(self, node):
            if node.name == candidate_name:
                node.name = replacement_name

    GlobalVarReplacer().visit(ast)
    return ast