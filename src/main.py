from mutations import *

import copy

import z3

import pcpp
from io import StringIO


from score_ast import *






# Early applicarion of AI --> MatEng
# Find the stat of interest; compare wrt this?
# Find stats of interest; evaluate wrt this; all behaviors you can compare...
# Code similarity metrics; output
# AST hamming distance
# Compare the control flow
# Explain how it works in the presentation
# Send introductory slides beforehand



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

    parser = c_parser.CParser()
    ast = parser.parse(c_code)

    ast = clean_and_preprocess(ast)

    #ast = opaquify(ast)
    #show_cfg(ast)

    ast = goto_if_stmt(ast)
    ast = goto_if_stmt(ast)
    ast = goto_if_stmt(ast)
    ast = goto_if_stmt(ast)
    ast = goto_if_stmt(ast)
    ast = goto_if_stmt(ast)

    #render_cfg(build_cfg_from_ast(ast))    



    render_cfg(gen_simplified_cfg(ast))    

    #ast = MC_mutate(ast)


    #render_cfg(build_cfg_from_ast(ast))
    #render_cfg(gen_simplified_cfg(ast))    


    generator = c_generator.CGenerator()

    code = generator.visit(ast)
    print("Generated code;\n", code)

    print(compile_c_code(code), compile_and_test(code))
    #show_cfg(ast)

if __name__ == "__main__":
    main()
