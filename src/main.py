from CFG import *
import os
import subprocess
import random

name_dict = []

def compile_c_code(source_file):
    compile_command = ["gcc", "-O3", "-c", source_file]
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
    # Create a new counter variable declaration node
    counter_var_name = rand_name()

    # Find a random position in the function body to insert the loop
    insert_position = random.randint(0, len(fxn.body.block_items))

    new_var_decl = c_ast.Decl(
        name="",
        quals=[],
        storage=[],
        funcspec=[],
        align=[],
        type=c_ast.TypeDecl(
            declname=counter_var_name,
            type=c_ast.IdentifierType(names=["int"]),
            quals=[],
            align=[]
        ),
        init=c_ast.Constant(type="int", value="0"),
        bitsize=None
    )

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
                    lvalue=c_ast.ID(name=counter_var_name),
                    rvalue=dummy
                )

                for dummy in make_dummy_statements(dummy_vars + [loop_var_name, counter_var_name])
            ]
        )
    )

    # Insert the new variable declaration and for loop at the beginning of the function body
    fxn.body.block_items.insert(-1, new_for_loop)
    fxn.body.block_items.insert(0, new_var_decl)
    return fxn, counter_var_name

def main():

    global name_dict
    name_dict = open("../words_alpha.txt", 'r').read().split("\n")

    name_dict = [i for i in name_dict if len(i) > 2]

    # Example C code including control flow constructs.
    c_code = r'''

    int f(int x)
    {
        return x * x * x * x;
    }

    int main() {

        int i = 0;
        int a = 0;
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

    #open("test.c","w+").write(c_code)
    #compile_c_code("test.c")
    #file_size = os.path.getsize('test.o')
    #print(f"Compiled file size: {file_size} bytes")

    parser = c_parser.CParser()
    ast = parser.parse(c_code)
    ast.ext[1], dummy1 = add_noop_var_decl(ast.ext[1])
    ast.ext[1], dummy2 = add_noop_var_decl(ast.ext[1])
    ast.ext[1], dummy3 = add_noop_var_decl(ast.ext[1])
    ast.ext[1], dummy4 = add_noop_var_decl(ast.ext[1])
    ast.ext[1], _ = add_dead_code(ast.ext[1], [dummy1, dummy2, dummy3, dummy4])

    generator = c_generator.CGenerator()
    print("Generated code;\n", generator.visit(ast))

if __name__ == "__main__":
    main()
