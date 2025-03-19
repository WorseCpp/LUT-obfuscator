
from qol import *

from preprocess import *

from opaque_op import opaquify, remove_oqaque_clauses

from globals import globalize_local, delete_global

import copy

import z3

import pcpp
from io import StringIO

from tqdm import tqdm

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

    print(target.type.type.names)

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



def MC_mutate(ast, itr = 250):

    ast = unique_locals(ast)

    for i in range(len(ast.ext)):
        ast.ext[i] = unroll_loops(ast.ext[i])


    for i in tqdm(range(itr)):
        old_ast = copy.deepcopy(ast)
        mode = random.randint(0, 100)

        if (mode < 25):
            # continue
            ast = globalize_local(ast)
        elif (mode < 30):
            # is own inverse
            ast = mutate_variable(ast)
        elif (mode < 97):
            # continue
            f = random.choice([opaquify, remove_oqaque_clauses])
            ast = f(ast)
        else:
            # continue
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

    init_rand_names()

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
    
    # ast = opaquify(ast)

  
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
