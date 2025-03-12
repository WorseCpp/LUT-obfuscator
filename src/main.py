from CFG import *
import os
import subprocess
import random
import copy

import z3

import pcpp
from io import StringIO

from tqdm import tqdm

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
    res = subprocess.run(compile_command, capture_output=True, text=True)
    if res.returncode != 0:
        return False
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
            break

    return fxn, label_name


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


class FunctionRenamer(c_ast.NodeVisitor):
    def __init__(self):
        self.counter = 1
        self.var_map = {}

    def visit_FuncDef(self, node):
        # Rename parameters.
        # print("Funcdef!!")
        func_type = node.decl.type
        if func_type.args:
            for param in func_type.args.params:
                if isinstance(param, c_ast.Decl):
                    new_name = f"var_{self.counter}"
                    self.var_map[param.name] = new_name
                    param.name = new_name
                    if isinstance(param.type, c_ast.TypeDecl):
                        param.type.declname = new_name

                    if isinstance(param.type, c_ast.ArrayDecl):
                        param.type.type.declname = new_name

                    if isinstance(param.type, c_ast.PtrDecl):
                        param.type.type.declname = new_name
                    
                    self.counter += 1
        # Process the function body.
        self.visit(node.body)

    def visit_Decl(self, node):
        # Rename a local variable declaration if it is not already renamed.
        if isinstance(node.type, c_ast.TypeDecl) and node.name and node.name not in self.var_map:
            new_name = f"var_{self.counter}"
            self.var_map[node.name] = new_name
            node.name = new_name
            node.type.declname = new_name
            self.counter += 1
        self.generic_visit(node)

    def visit_ID(self, node):
        # Replace identifier usage with its new unique name.
        if node.name in self.var_map:
            node.name = self.var_map[node.name]

def unique_locals(ast):
    # Process each function definition independently.
    renamer = FunctionRenamer()
    renamer.visit(ast)
    return ast

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

def create_binary_op(names, n):
    if (len(names) < 2):
        return c_ast.Constant(type="int", value="0")

    # loosely try to make a real issue
    first = random.choice(names)
    ctr = c_ast.BinaryOp(op = "*", left = first, right = first)

    for i in range(1, n):
        ctr = c_ast.BinaryOp(op = "*", left = ctr, right = c_ast.BinaryOp(op = "+", left = first, right = c_ast.Constant(type="int", value=i)))

    return c_ast.BinaryOp(op="%", left=ctr, right = c_ast.Constant(type="int", value=n))

    
def mutate_variable(ast):

    # Collect global declarations that are not function definitions.
    globals_decl = [node for node in ast.ext if isinstance(node, c_ast.Decl) and not isinstance(node.type, c_ast.FuncDecl)]
    if not globals_decl:
        return ast

    # Randomly choose one global variable.
    target = random.choice(globals_decl)

    # Only proceed if the type is a TypeDecl.
    if not isinstance(target.type, c_ast.TypeDecl):
        return ast

    # Get the current type names.
    current_type = target.type.type.names

    mutations = ["volatile", "extern", "unsigned", "long"]

    mutation = random.choice(mutations)
    if mutation not in target.type.type.names:
        target.type.type.names.append(mutation)

    return ast

def opaquify(ast):

    # Filter functions that have a body with statements.
    valid_funcs = [f for f in ast.ext if hasattr(f, "body") and f.body and getattr(f.body, "block_items", None)]
    
    if not valid_funcs:
        return ast

    while valid_funcs:
        # Select a random function.
        selected_func = random.choice(valid_funcs)

        valid_funcs.remove(selected_func)

        # Filter statements in the function's body that are either an assignment or an if statement.
        candidates = [stmt for stmt in selected_func.body.block_items
                        if isinstance(stmt, (c_ast.Assignment, c_ast.If, c_ast.For, c_ast.While, c_ast.Decl))]
        
        if not candidates and not valid_funcs:
            return ast

    # Select a random statement from the candidates.
    selected_stmt = random.choice(candidates)
#    print(selected_stmt)

    to_be_opaquified = None

    if isinstance(selected_stmt, c_ast.Decl):
        gen = c_generator.CGenerator()
        decl_type = gen.visit(selected_stmt.type)
        if selected_stmt.init is not None:
            to_be_opaquified = selected_stmt.init
        else:
            raise Exception("Declaration without initialization not supported")
    elif isinstance(selected_stmt, (c_ast.If, c_ast.For, c_ast.While)):
        to_be_opaquified = selected_stmt.cond
    else:
        to_be_opaquified = selected_stmt.rvalue


    global_vars = [c_ast.ID(name=decl.name) for decl in ast.ext
                   if isinstance(decl, c_ast.Decl) and not isinstance(decl.type, c_ast.FuncDecl)]
    local_vars = [c_ast.ID(name=decl.name) for decl in selected_func.body.block_items
                  if isinstance(decl, c_ast.Decl)]

    # todo; generate these on-the-fly
    opaque_expr = create_binary_op(global_vars + local_vars, random.randint(2, 5))

    # print(selected_stmt,"\n", opaque_expr)
    # print(selected_stmt, "\nOpq:\n", opaque_expr)
    if isinstance(selected_stmt, c_ast.Decl):
        selected_stmt.init = c_ast.BinaryOp(op = " + ", left = selected_stmt.init, right = opaque_expr)
    elif isinstance(selected_stmt, (c_ast.If, c_ast.For, c_ast.While)):
        selected_stmt.cond = c_ast.BinaryOp(op = " || ", left = selected_stmt.cond, right = opaque_expr)
    else:
        selected_stmt.rvalue = c_ast.BinaryOp(op = "+", left = selected_stmt.rvalue, right = opaque_expr)

    return ast

def MC_mutate(ast, itr = 250):

    ast = unique_locals(ast)

    for i in range(len(ast.ext)):
        ast.ext[i], _ = add_goto_delete_for(ast.ext[i])
        ast.ext[i], _ = add_goto_delete_while(ast.ext[i])

    for i in tqdm(range(itr)):
        old_ast = copy.deepcopy(ast)
        mode = random.randint(0, 100)

        if (mode < 25):
            ast = globalize_local(ast)
        elif (mode < 50):
            ast = mutate_variable(ast)
        elif (mode < 95):
            ast = opaquify(ast)
        else:
            ast = goto_if_stmt(ast)
        
        generator = c_generator.CGenerator()

        code = generator.visit(ast)
        if (not compile_and_test(code)):
            ast = old_ast

    return ast

def main():

    s = random.randbytes(5)
    s = b'\x93e\x0c\xb9\xf3'
    random.seed(s)

    global name_dict

    name_dict = open("../words_alpha.txt", 'r').read().split("\n")
    name_dict = [i for i in name_dict if len(i) > 2]

    # Example C code including control flow constructs.
    c_code = r'''
        void swap(int *a, int *b) {

            int temp = *a;

            *a = *b;

            *b = temp;

        }

        int partition(int arr[], int low, int high) {

            int pivot = arr[high];

            int i = (low - 1);

            for (int j = low; j <= high - 1; j++) {

                if (arr[j] <= pivot) {

                    i++;

                    swap(&arr[i], &arr[j]);

                }

            }

            swap(&arr[i + 1], &arr[high]);

            return (i + 1);

        }



        void quickSort(int arr[], int low, int high) {

            if (low < high) {

                int pi = partition(arr, low, high);

                quickSort(arr, low, pi - 1);
                quickSort(arr, pi + 1, high);

            }

        }
    '''

    pp = pcpp.Preprocessor()
    pp.parse(c_code)
    output = StringIO()
    pp.write(output)
    c_code = output.getvalue()

    #print(c_code)

    #print(compile_and_test(c_code))

    #open("test.c","w+").write(c_code)
    #compile_c_code("test.c")
    #file_size = os.path.getsize('test.o')
    #print(f"Compiled file size: {file_size} bytes")

    parser = c_parser.CParser()
    ast = parser.parse(c_code)

    #ast = opaquify(ast)

    ast = MC_mutate(ast)

    # ast = delete_global(ast)
    
    # ast.ext[1],_ = add_goto_delete_for(ast.ext[1])
    # ast = goto_if_stmt(ast)



    generator = c_generator.CGenerator()

    code = generator.visit(ast)
    print("Generated code;\n", code)

    print(compile_c_code(code), compile_and_test(code))
    show_cfg(ast)

if __name__ == "__main__":
    main()
