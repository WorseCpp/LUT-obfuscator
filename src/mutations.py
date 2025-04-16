import copy 

from qol import *

from preprocess import *

from tqdm import tqdm

from opaque_op import opaquify, remove_oqaque_clauses

from globals import globalize_local, delete_global

def goto_if_stmt(ast):
    # Pick all function definitions from the AST.
    func_defs = [node for node in ast.ext if isinstance(node, c_ast.FuncDef)]
    if not func_defs:
        return ast

    # Select a random function.
    selected_func = random.choice(func_defs)

    # Ensure the function has a body with statements.
    if not selected_func.body or not selected_func.body.block_items:
        return ast

    # Find all if statements in the function body.
    if_stmts = [stmt for stmt in selected_func.body.block_items if isinstance(stmt, c_ast.If)]
    if not if_stmts:
        return ast

    # Select a random if statement.
    if_stmt = random.choice(if_stmts)

    # Create a unique label name using rand_name().
    true_label_name = rand_name()

    false_label_name = rand_name()

    end_label_name = rand_name()

    i = selected_func.body.block_items.index(if_stmt)

    goto_true = c_ast.Goto(name=true_label_name)

    goto_false = c_ast.Goto(name=false_label_name)

    goto_end = c_ast.Goto(name=end_label_name)

    new_if = c_ast.If(
        cond=if_stmt.cond,
        iftrue= c_ast.Compound(block_items=[goto_true]),
        iffalse=c_ast.Compound(block_items=[goto_false])
    )

    true_label = c_ast.Label(
        name=true_label_name,
        stmt=c_ast.Compound(block_items=[])
    )

    true_bloc = [true_label, if_stmt.iftrue, goto_end] if if_stmt.iftrue else [true_label, goto_end]

    false_label = c_ast.Label(
        name=false_label_name,
        stmt=c_ast.Compound(block_items=[])
    )

    false_bloc = [false_label, if_stmt.iffalse] if if_stmt.iffalse else [false_label]

    def unpack_bloc(bloc):
        new_bloc = []
        for stmt in bloc:
            if isinstance(stmt, c_ast.Compound) and stmt.block_items is not None:
                new_bloc += (stmt.block_items)
            else:
                new_bloc.append(stmt)
        return new_bloc

    true_bloc = unpack_bloc(true_bloc)
    false_bloc = unpack_bloc(false_bloc)

    end_label = c_ast.Label(
        name = end_label_name,
        stmt = c_ast.Compound(block_items=[])
    )

    selected_func.body.block_items[i] = new_if

    for stmt in ((true_bloc)):
        selected_func.body.block_items.insert(i + 1, stmt)
        i += 1

    for stmt in ((false_bloc)):
        selected_func.body.block_items.insert(i + 1, stmt)
        i += 1

    selected_func.body.block_items.insert(i + 1, end_label)
    
    return ast

def dummy_operation(ast):
    # Pick all function definitions from the AST.
    func_defs = [node for node in ast.ext if isinstance(node, c_ast.FuncDef)]
    if not func_defs:
        return ast

    # Select a random function.
    selected_func = random.choice(func_defs)

    # Ensure the function has a body with statements.
    if not selected_func.body or not selected_func.body.block_items:
        return ast
    

    # Select a random global variable.
    globals_decl = [
        node for node in ast.ext
        if isinstance(node, c_ast.Decl) and not isinstance(node.type, c_ast.FuncDecl)
    ]
    if not globals_decl:
        return ast
    global_var = random.choice(globals_decl)
    
    # Retrieve the variable name from the global declaration.
    var_name = global_var.name

    # Create a dummy assignment: assign the value 42 to the global variable.
    dummy_assignment = c_ast.Assignment(
        op="=",
        lvalue=c_ast.ID(name=var_name),
        rvalue=c_ast.Constant(type="int", value="42")
    )

    #print("Dummy assignment:", dummy_assignment)
    #print(selected_func.decl.name)

    # Insert the dummy assignment at the beginning of the selected function's body.
    insert_index = random.randint(0, len(selected_func.body.block_items))
    selected_func.body.block_items.insert(insert_index, dummy_assignment)
    
    return ast

def conditionalize_goto(ast):
    # Select a random function definition.
    func_defs = [node for node in ast.ext if isinstance(node, c_ast.FuncDef)]
    if not func_defs:
        return ast
    selected_func = random.choice(func_defs)
    if not selected_func.body or not getattr(selected_func.body, "block_items", None):
        return ast

    # Locate all goto statements in the function body.
    goto_candidates = [(i, stmt) for i, stmt in enumerate(selected_func.body.block_items)
                        if isinstance(stmt, c_ast.Goto)]
    if not goto_candidates:
        return ast

    # Select a random goto statement.
    index, goto_stmt = random.choice(goto_candidates)

    # Create an if(true) statement enclosing the goto.
    true_condition = c_ast.Constant(type="int", value="1")
    new_if = c_ast.If(
        cond=true_condition,
        iftrue=c_ast.Compound(block_items=[goto_stmt]),
        iffalse=None
    )

    # Replace the original goto with the new if statement.
    selected_func.body.block_items[index] = new_if

    return ast

def inverse_conditionalize_goto(ast):
    # Select a random function definition.
    func_defs = [node for node in ast.ext if isinstance(node, c_ast.FuncDef)]
    if not func_defs:
        return ast
    selected_func = random.choice(func_defs)
    if not selected_func.body or not getattr(selected_func.body, "block_items", None):
        return ast

    # Locate candidate if statements with condition constant "1".
    if_candidates = [(i, stmt) for i, stmt in enumerate(selected_func.body.block_items)
                        if isinstance(stmt, c_ast.If)
                        and isinstance(stmt.cond, c_ast.Constant)
                        and stmt.cond.type == "int"
                        and stmt.cond.value == "1"]
    if not if_candidates:
        return ast

    # Select a random candidate.
    index, if_stmt = random.choice(if_candidates)

    # Ensure the if has a Compound for its true branch.
    if not if_stmt.iftrue or not isinstance(if_stmt.iftrue, c_ast.Compound):
        return ast

    # Retrieve the list of statements from the iftrue branch.
    block_items = if_stmt.iftrue.block_items or []

    # Remove the if statement and insert its body's statements at the same position.
    del selected_func.body.block_items[index]
    for stmt in reversed(block_items):
        selected_func.body.block_items.insert(index, stmt)
    return ast

def mutate_variable(ast):

    # Collect global declarations that are not function definitions.
    globals_decl = [node for node in ast.ext if isinstance(node, c_ast.Decl) and not isinstance(node.type, c_ast.FuncDecl)]

    # Randomly choose one variable, either from globals or local variables in a function.
    function_defs = [node for node in ast.ext if isinstance(node, c_ast.FuncDef)]
    local_decls = []
    if function_defs:
        selected_func = random.choice(function_defs)
        if selected_func.body and getattr(selected_func.body, "block_items", None):
            local_decls = [stmt for stmt in selected_func.body.block_items if isinstance(stmt, c_ast.Decl)]
    all_vars = globals_decl + local_decls
    
    if not all_vars:
        return ast
    target = random.choice(all_vars)

    
    # Only proceed if the type is a TypeDecl.
    if not isinstance(target.type, c_ast.TypeDecl):
        return ast

    # Get the current type names.
    current_type = target.type.type.names

    mutations = ["volatile", "extern", "unsigned", "long"]

    m_types = ["int", "char", "float", "double"]

    roll = random.random()

    #print(target.type.type.names)

    if (roll < .3):
        mutation = random.choice(mutations)
        if mutation not in target.type.type.names:
            target.type.type.names.append(mutation)
    elif roll < .6:
        l = target.type.type.names
        l2 = []
        for entry in l:
            for t in m_types:
                if (t in entry):
                    l2.append(random.choice(m_types))
            if (not (entry in l2)):
                l2.append(entry)
        target.type.type.names = l2
    else:
        l = target.type.type.names
        l2 = []
        for entry in l:
            for t in m_types:
                if (t in entry):
                    l2.append(entry)
            if (not (entry in l2) and random.random() > .5):
                l2.append(entry)
        target.type.type.names = l2
        
    return ast

def clean_and_preprocess(ast):
    ast = unique_locals(ast)

    for i in range(len(ast.ext)):
        ast.ext[i] = unroll_loops(ast.ext[i])
    return ast

def MC_mutate(ast, itr = 250):

    fail_n = 1

    ast = clean_and_preprocess(ast)


    m_itr = 0
    n_itr = 1
    generator = c_generator.CGenerator()


    for i in tqdm(range(itr)):
        
        if (m_itr == 0):
            old_ast = copy.deepcopy(ast)

        if (m_itr < n_itr):

            mode = random.randint(0, 100)

            if (mode < 10):
                # continue
                ast = globalize_local(ast)
            elif (mode < 10):
                # is own inverse
                ast = mutate_variable(ast)
            elif (mode < 20):
                ast = dummy_operation(ast)
            elif (mode < 30):
                if (random.random() > .5):
                    ast = conditionalize_goto(ast)
                else:
                    ast = inverse_conditionalize_goto(ast)
            elif (mode < 90):
                # continue
                f = random.choice([opaquify, remove_oqaque_clauses])
                ast = f(ast)
            else:
                # continue
                ast = goto_if_stmt(ast)

            m_itr += 1
            
        else:

            code = generator.visit(ast)
            if (not compile_and_test(code)):
                #print("Fail!\n")
                ast = old_ast
                fail_n += m_itr

            m_itr = 0
            n_itr = i / fail_n
            

    return (old_ast, ast)[compile_and_test(generator.visit(ast))]