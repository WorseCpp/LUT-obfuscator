from CFG import *
import os
import subprocess
import random
import copy

name_dict = []

def compile_c_code(code, v = True):
    open("code.c","w+").write(code)
    compile_command = ["gcc", "-O3", "-c", "code.c"]
    result = subprocess.run(compile_command, capture_output=True, text=True)
    if result.returncode != 0:
        if (v):
            print(f"Compilation failed: {result.stderr}")
        return False
    else:
        if v:
            print(f"Compilation succeeded: {result.stdout}")
        return True

def compile_and_test(code):
    if not compile_c_code(code, False):
        return False
    compile_command = ["gcc", "-O3", "-o", "out", "main.o", "code.o"]
    subprocess.run(compile_command, capture_output=True, text=True)
    test_cmd = ["./out"]
    res = subprocess.run(test_cmd, capture_output=True, text=True)
    return bool(res.returncode)


def show_cfg(c_code):
    

    parser = c_parser.CParser()
    ast = parser.parse(c_code)

    generator = c_generator.CGenerator()
    print("Generated code;\n", generator.visit(ast))
    
    cfg = CFG()
    
    # Process each function definition in the AST.
    for ext in ast.ext:
        if isinstance(ext, c_ast.FuncDef):
            build_cfg_from_func(ext, cfg)
    
    # Render and view the CFG as a PNG image.
    cfg.dot.render("c_cfg", format="png", view=True)

def show_cfg(ast):
    cfg = CFG()
    
    # Process each function definition in the AST.
    for ext in ast.ext:
        if isinstance(ext, c_ast.FuncDef):
            build_cfg_from_func(ext, cfg)
    
    # Render and view the CFG as a PNG image.
    cfg.dot.render("c_cfg", format="png", view=True)

def rand_name():
    choice = random.choice(name_dict)
    name_dict.remove(choice)
    return choice

def add_noop_var_decl(fxn):
    # Create a new variable declaration node
    noop_var_name = rand_name()

    new_var_decl = c_ast.Decl(
        name="",
        quals=[],
        storage=[],
        funcspec=[],
        align=[],
        type=c_ast.TypeDecl(
            declname=noop_var_name,
            type=c_ast.IdentifierType(names=["int"]),
            quals=[],
            align=[]
        ),
        init=c_ast.Constant(type="int", value=str(random.randint(-2**16, 2**16))),
        bitsize=None
    )

    # Insert the new variable declaration at the beginning of the function body
    fxn.body.block_items.insert(0, new_var_decl)
    return fxn, noop_var_name

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

            break
    return fxn, label_name


operations = ['+', '-', '*', '/', '%', '|', '||', '&', '&&']


def make_dummy_statements(dummy_vars):
    dummy_statements = []
    
    for var in dummy_vars:
        op = random.choice(operations)
        value = random.randint(1, 10)
        dummy_statements.append(
            c_ast.Assignment(
                op=op,
                lvalue=c_ast.ID(name=var),
                rvalue=c_ast.Constant(type="int", value=str(value))
            )
        )
    

    node = c_ast.Assignment(
                        op=random.choice(operations) + "=",
                        lvalue=c_ast.ID(name=random.choice(dummy_vars)),
                        rvalue=dummy_vars
                    )

    return dummy_statements

def add_dead_code(fxn, dummy_vars):
    # Find a random position in the function body to insert the loop
    insert_position = random.randint(0, len(fxn.body.block_items))


    # Create a new for loop node
    loop_var_name = rand_name()
    new_for_loop = c_ast.For(
        init=c_ast.DeclList(
            decls=[c_ast.Decl(
                name="",
                quals=[],
                storage=[],
                funcspec=[],
                align=[],
                type=c_ast.TypeDecl(
                    declname=loop_var_name,
                    type=c_ast.IdentifierType(names=["int"]),
                    quals=[],
                    align=[]
                ),
                init=c_ast.Constant(type="int", value="0"),
                bitsize=None
            )]
        ),
        cond=c_ast.BinaryOp(
            op="<",
            left=c_ast.ID(name=loop_var_name),
            right=c_ast.Constant(type="int", value=str(random.randint(2, 5)))
        ),
        next=c_ast.UnaryOp(
            op="++",
            expr=c_ast.ID(name=loop_var_name)
        ),
        stmt=c_ast.Compound(
            block_items=[
                
                c_ast.Assignment(
                    op=random.choice(operations) + "=",
                    lvalue=c_ast.ID(name=random.choice(dummy_vars)),
                    rvalue=dummy
                )

                for dummy in random.sample(make_dummy_statements(dummy_vars + [loop_var_name]), min(len(dummy_vars), 5))
            ]
        )
    )

    # Insert the new variable declaration and for loop at the beginning of the function body
    fxn.body.block_items.insert(-1, new_for_loop)
    return fxn, None

def add_global(ast, typ='int'):
    # Create a new global variable declaration node
    global_var_name = rand_name()

    new_global_var_decl = c_ast.Decl(
        name="",
        quals=[],
        storage=[],
        funcspec=[],
        align=[],
        type=c_ast.TypeDecl(
            declname=global_var_name,
            type=c_ast.IdentifierType(names=[typ]),
            quals=['static'],
            align=[]
        ),
        init=c_ast.Constant(type=typ, value=str(random.randint(-2**16, 2**16))),
        bitsize=None
    )

    # Insert the new global variable declaration at the beginning of the AST
    ast.ext.insert(0, new_global_var_decl)
    return ast, global_var_name


def globalize(ast):
    new_globals = []

    def extract_decls(compound):
        if not hasattr(compound, "block_items") or compound.block_items is None:
            return
        retained = []
        for item in compound.block_items:
            # If the item is a local variable declaration (skip function declarations)
            if isinstance(item, c_ast.Decl) and not isinstance(item.type, c_ast.FuncDecl):
                new_globals.append(item)
            else:
                retained.append(item)
                # Recursively check any nested compound statement
                if hasattr(item, "block_items") and item.block_items:
                    extract_decls(item)
                else:
                    for _, child in item.children():
                        if isinstance(child, c_ast.Compound):
                            extract_decls(child)
        compound.block_items = retained

    # Process each function definition's body
    ext = random.choice(ast.ext)
    if isinstance(ext, c_ast.FuncDef):
        extract_decls(ext.body)

    # Prepend the extracted local declarations as globals
    ast.ext = new_globals + ast.ext

    return ast


def noarg(ast):
    # Pick a random function that has parameters.
    func_defs = [node for node in ast.ext if isinstance(node, c_ast.FuncDef) and node.decl.type.args and node.decl.type.args.params]
    
    if not func_defs:
        return ast
    chosen_fx = random.choice(func_defs)
    
    func_name = chosen_fx.decl.name
    params = chosen_fx.decl.type.args.params


    # Gather existing globals (non-function declarations) from the AST.
    existing_globals = [d for d in ast.ext if isinstance(d, c_ast.Decl) and not isinstance(d, c_ast.FuncDef)]
    global_map = {}  # maps parameter name to the global variable name

    def get_type_str(decl):
        if isinstance(decl.type, c_ast.TypeDecl) and isinstance(decl.type.type, c_ast.IdentifierType):
            return " ".join(decl.type.type.names)
        return ""

    for param in params:
        typ = get_type_str(param)
        new_global_decl = c_ast.Decl(
            name="",
            quals=[],
            storage=[],
            funcspec=[],
            align=[],
            type=c_ast.TypeDecl(
                declname=param.name,
                type=c_ast.IdentifierType(names=[typ]),
                quals=[],
                align=[]
            ),
            init=c_ast.Constant(type=typ, value="0"),
            bitsize=None
        )
        ast.ext.insert(0, new_global_decl)
        global_map[param.name] = param.name

    # Fully traverse the AST using an iterative loop.
    nodes_to_visit = [(ast, None, 0)]
    while nodes_to_visit:
        current_node, last_parent, m_pos = nodes_to_visit.pop()
        # Example processing: if current node is a function call, print it along with the last parent
        if isinstance(current_node, c_ast.FuncCall):
            if current_node.args and isinstance(current_node.args, c_ast.ExprList):
                for i, arg in enumerate(current_node.args.exprs):
                    assign_stmt = c_ast.Assignment(
                        op="=",
                        lvalue=c_ast.ID(name=params[i].name),
                        rvalue=arg
                    )

                    
                    if hasattr(last_parent, "block_items"):
                        last_parent.block_items.insert(m_pos, assign_stmt)
                    elif hasattr(last_parent, "body") and hasattr(last_parent.body, "block_items"):
                        last_parent.body.block_items.insert(m_pos, assign_stmt)

        for i, tu in enumerate(current_node.children()):
            _, child = tu
            # If the current node has a body with block_items, update last_parent; otherwise, propagate the existing one.
            if hasattr(current_node, "body") and hasattr(current_node.body, "block_items"):
                new_parent = current_node
                new_pos = i
            elif hasattr(current_node, "block_items"):
                new_parent = current_node
                new_pos = i
            else:
                new_parent = last_parent
                new_pos = m_pos
            nodes_to_visit.append((child, new_parent, new_pos))

    nodes_to_visit = [ast]
    while nodes_to_visit:
        current = nodes_to_visit.pop()
        for _, child in current.children():
            nodes_to_visit.append(child)
        if isinstance(current, c_ast.FuncCall):
            current.args = None

    chosen_fx.decl.type.args = None

    return ast

def transplant_block(ast):
    # Select function definitions randomly.
    func_defs = [node for node in ast.ext if isinstance(node, c_ast.FuncDef)]
    if len(func_defs) < 1:
        return ast
    fxn= random.choice(func_defs)

    # In the first function, pick a random block (a statement) to replace.
    if not fxn.body or not fxn.body.block_items:
        return ast
    
    if (len(fxn.body.block_items) < 3):
        return ast;

    block_begin = random.randint(0, len(fxn.body.block_items) - 2)
    block_end = random.randint(block_begin, len(fxn.body.block_items) - 1)
    target_block = fxn.body.block_items[block_begin:block_end]

    label_before = rand_name()
    label_after = rand_name()

    pre_block = fxn.body.block_items[:block_begin]
    target = fxn.body.block_items[block_begin:block_end]
    post_block = fxn.body.block_items[block_end:]

    goto_to_target = c_ast.Goto(name=label_before)

    target_label = c_ast.Label(
        name=label_before,
        stmt=c_ast.Compound(
            block_items=pre_block + target + [c_ast.Goto(name=label_after)]
        )
    )

    after_label = c_ast.Label(
        name=label_after,
        stmt=c_ast.Compound(
            block_items=post_block
        )
    )

    fxn.body.block_items = [goto_to_target, after_label] + [target_label];
    return ast

def uniquefy(ast):
    counter = 1

    def new_name():
        nonlocal counter
        name = f"var_{counter}"
        counter += 1
        return name

    def visit(node, env):
        # If node introduces a new block scope, push a new scope map.
        if isinstance(node, c_ast.Compound):
            env.append({})
            if getattr(node, "block_items", None):
                for child in node.block_items:
                    visit(child, env)
            env.pop()
        # Process local variable declarations.
        elif isinstance(node, c_ast.Decl) and getattr(node, "name", None):
            old_name = node.name
            unique = new_name()
            node.name = unique
            if hasattr(node.type, "declname"):
                node.type.declname = unique
            env[-1][old_name] = unique
            for _, child in node.children():
                visit(child, env)
        # Update identifiers using the current environment stack.
        elif isinstance(node, c_ast.ID):
            for scope in reversed(env):
                if node.name in scope:
                    node.name = scope[node.name]
                    break
        else:
            for _, child in node.children():
                visit(child, env)

    for ext in ast.ext:
        if isinstance(ext, c_ast.FuncDef):
            # Set up a scope for function parameters.
            env = [{}]
            if ext.decl.type.args and ext.decl.type.args.params:
                for param in ext.decl.type.args.params:
                    if getattr(param, "name", None):
                        old_name = param.name
                        unique = new_name()
                        param.name = unique
                        if hasattr(param.type, "declname"):
                            param.type.declname = unique
                        env[0][old_name] = unique
            visit(ext.body, env)
    return ast

def rm_global(ast):
    # Gather global declarations (non-function declarations)
    globals_list = [g for g in ast.ext if isinstance(g, c_ast.Decl) and not isinstance(g, c_ast.FuncDef)]
    if len(globals_list) < 2:
        return ast

    # Select a global randomly to remove
    removed_global = random.choice(globals_list)

    # Helper to extract type string from a declaration
    def get_type_str(decl):
        try:
            return " ".join(decl.type.type.names)
        except AttributeError:
            return ""

    removed_type = get_type_str(removed_global)

    # Find other globals of the same type
    candidate_globals = [g for g in globals_list if g is not removed_global and get_type_str(g) == removed_type]
    if not candidate_globals:
        return ast

    replacement_global = random.choice(candidate_globals)

    # Determine variable names to replace
    removed_name = removed_global.type.declname if hasattr(removed_global.type, "declname") else removed_global.name
    replacement_name = replacement_global.type.declname if hasattr(replacement_global.type, "declname") else replacement_global.name

    # Remove the chosen global from the list of globals
    ast.ext.remove(removed_global)

    # Traverse the AST and replace identifiers
    def replace_identifiers(node):
        if isinstance(node, c_ast.ID) and node.name == removed_name:
            node.name = replacement_name
        for _, child in node.children():
            replace_identifiers(child)

    for node in ast.ext:
        replace_identifiers(node)

    return ast

def main():
    #random.seed(1)

    global name_dict
    name_dict = open("../words_alpha.txt", 'r').read().split("\n")
    name_dict = [i for i in name_dict if len(i) > 2]

    # Example C code including control flow constructs.
    c_code = r'''

        int fib(int i) {
            int a = 1;
            int b = 1;
            int c = a + b;

            if (i == 0 | i == 1)
            {
            return 1;
            }

            if (i >= 20)
            {
                return -1;
            }

            for (int j = 0; j < i - 2; j++)
            {
                a = b;
                b = c;
                c = a + b;
            }    
            return c;
        }

        float sqr(float x)
        {
            return x*x;    
        }

        float ring(float x)
        {
            float ctr = 0;
            for (int i = 0; i < 3; i++)
            {
                ctr = sqr(ctr + x);
            }
            return ctr;
        }
    '''

    print(compile_and_test(c_code))

    #open("test.c","w+").write(c_code)
    #compile_c_code("test.c")
    #file_size = os.path.getsize('test.o')
    #print(f"Compiled file size: {file_size} bytes")

    parser = c_parser.CParser()
    ast = parser.parse(c_code)
    # clean AST
    ast = uniquefy(ast) # unique variable names

    generator = c_generator.CGenerator()

    for i in range(100):
        a = random.randint(0, 3)
        old_ast = copy.deepcopy(ast)
        new_ast = None
        if (a < 1):
            new_ast = globalize(ast) # ONLY globals
        elif (a < 2):
            new_ast = noarg(ast) #No argument passing :D
        elif (a < 3):
            new_ast = ast
            ch = random.randint(0, len(new_ast.ext)-1)
            new_ast.ext[ch] = add_dead_code(new_ast.ext[ch], ())
        else:
            new_ast = rm_global(ast)

        if (compile_and_test(generator.visit(new_ast))):
            # print("swap")
            ast = new_ast
            assert(compile_and_test(generator.visit(ast)))
        else:
            ast = old_ast


    code = generator.visit(ast)
    print("Generated code;\n", code)

    print(compile_c_code(code), compile_and_test(code))

if __name__ == "__main__":
    main()
