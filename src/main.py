from CFG import *
import os
import subprocess
import random

name_dict = []

def compile_c_code(code):
    open("code.c","w+").write(code)
    compile_command = ["gcc", "-O3", "-c", "code.c"]
    result = subprocess.run(compile_command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Compilation failed: {result.stderr}")
    else:
        print(f"Compilation succeeded: {result.stdout}")

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

def add_global(ast):
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
            type=c_ast.IdentifierType(names=["int"]),
            quals=['static'],
            align=[]
        ),
        init=c_ast.Constant(type="int", value=str(random.randint(-2**16, 2**16))),
        bitsize=None
    )

    # Insert the new global variable declaration at the beginning of the AST
    ast.ext.insert(0, new_global_var_decl)
    return ast, global_var_name

def globalization(ast):
    # Choose a random function definition from the AST.
    func_defs = [node for node in ast.ext if isinstance(node, c_ast.FuncDef)]
    if not func_defs:
        return ast
    chosen_fx = random.choice(func_defs)

    if not chosen_fx.body or not chosen_fx.body.block_items:
        return ast

    # Collect local variable declarations from the chosen function.
    local_decls = []
    new_block_items = []
    for item in chosen_fx.body.block_items:
        if isinstance(item, c_ast.Decl):
            local_decls.append(item)
        else:
            new_block_items.append(item)
    chosen_fx.body.block_items = new_block_items

    # Move each local declaration to the global AST scope.
    for decl in local_decls:
        # Mark as 'static' to indicate global scope if not already set.
        if hasattr(decl, 'quals'):
            if 'static' not in decl.quals:
                decl.quals.append('static')
        else:
            decl.quals = ['static']
        ast.ext.insert(0, decl)

    return ast


def noarg(ast, globals):

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

    # For each parameter, see if a global of the same type exists.
    for param in params:
        param_type = get_type_str(param)
        if not param_type:
            continue
        found = None
        for g in existing_globals:
            if get_type_str(g) == param_type:
                # Use the global variable's declared name.
                if isinstance(g.type, c_ast.TypeDecl):
                    found = g.type.declname
                break
        if found:
            global_map[param.name] = found
        else:
            # Create a new global variable using the parameter name.
            new_global = c_ast.Decl(
                name="",
                quals=['static'],
                storage=[],
                funcspec=[],
                align=[],
                type=c_ast.TypeDecl(
                    declname=param.name,
                    type=param.type.type,
                    quals=[],
                    align=[]
                ),
                init=None,
                bitsize=None
            )
            ast.ext.insert(0, new_global)
            global_map[param.name] = param.name
            existing_globals.append(new_global)

    # Remove all parameters from the chosen function.
    chosen_fx.decl.type.args.params = []

    # Save the original parameters and then clear them from the function definition.
    original_params = list(params)
    chosen_fx.decl.type.args.params = []

    
    return ast

def main():

    random.seed(0)

    global name_dict
    name_dict = open("../words_alpha.txt", 'r').read().split("\n")

    name_dict = [i for i in name_dict if len(i) > 2]

    # Example C code including control flow constructs.
    c_code = r'''

    int g(int x)
    {
        float i = 0;
        i = x * x;
        return i*8;
    }

    int f(int x)
    {
        return x * x * x * x;
    }

    int main() {

        int i = 0;
        int a = 0;
        int j = 0;
        j = f(10);
        if (a < 10) {
            a = a + 1;
        } else {
            a = a - 1;
        }
        while (a < 15) {
            a++;
            i += f(a);
        }
        return a;
    }
    '''

    compile_c_code(c_code)

    #open("test.c","w+").write(c_code)
    #compile_c_code("test.c")
    #file_size = os.path.getsize('test.o')
    #print(f"Compiled file size: {file_size} bytes")

    parser = c_parser.CParser()
    ast = parser.parse(c_code)
    ast = globalization(ast)
    ast = noarg(ast, [])

    generator = c_generator.CGenerator()
    print("Generated code;\n", generator.visit(ast))

    compile_c_code(generator.visit(ast))

if __name__ == "__main__":
    main()
