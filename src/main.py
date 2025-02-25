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

            label.stmt.block_items.append(c_ast.If(
                    cond=stmt.cond,
                    iftrue=c_ast.Compound(block_items=[]),
                    iffalse=c_ast.Compound(block_items=[c_ast.Goto(name=end_label_name)])
                ))

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
            break

    return fxn, label_name



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

    ast.ext[0], _ = add_goto_delete_for(ast.ext[0])
    ast.ext[2], _ = add_goto_delete_for(ast.ext[2])

    generator = c_generator.CGenerator()

    code = generator.visit(ast)
    print("Generated code;\n", code)

    print(compile_c_code(code), compile_and_test(code))

if __name__ == "__main__":
    main()
