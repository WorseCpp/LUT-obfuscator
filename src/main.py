from mutations import *

import copy

import z3

import pcpp
from io import StringIO


from score_ast import *
import pickle
import numpy as np

import matplotlib.pyplot as plt
# Early applicarion of AI --> MatEng
# Find the stat of interest; compare wrt this?
# Find stats of interest; evaluate wrt this; all behaviors you can compare...
# Code similarity metrics; output
# AST hamming distance
# Compare the control flow
# Explain how it works in the presentation
# Send introductory slides beforehand

def characterize_edit_dist(ast):
    
    x = list(np.linspace(0, 100, 5)) + list(np.linspace(100, 1000, 5))
    print(x)
    
    old_ast = copy.deepcopy(ast)

    y = []

    for itr in x:

        d = []

        for _ in range(10):
            ast = MC_mutate(copy.deepcopy(old_ast), int(itr) + 1)

            cfg_1 = build_cfg_from_ast(old_ast)
            cfg_2 = build_cfg_from_ast(ast)

            old_cfg = simplify_cfg_graph(cfg_1)
            new_cfg = simplify_cfg_graph(cfg_2)

            #render_cfg(old_cfg)
            #render_cfg(new_cfg)
            d.append(graph_edit_distance(old_cfg, new_cfg))

        y.append(np.mean(d))
        print(y)


    plt.plot(x, y)
    plt.xlabel("Steps")
    plt.ylabel("CFG Edit Distance (average of 5)")
    plt.title("Simplified CFG Edit Distance vs Steps")
    plt.savefig("fig.png")
    plt.show()

def proc_edit_dist_data():
    y= [np.float64(0.6), np.float64(10.3), np.float64(15.6), np.float64(24.1), np.float64(29.9), np.float64(24.4), np.float64(40.2), np.float64(65.3), np.float64(67.9), np.float64(80.2)]
    x = [np.float64(0.0), np.float64(25.0), np.float64(50.0), np.float64(75.0), np.float64(100.0), np.float64(100.0), np.float64(325.0), np.float64(550.0), np.float64(775.0), np.float64(1000.0)]

    y = np.array(y)
    x = np.array(x)
    s_x = np.sqrt(x)

    m,b = np.polyfit(s_x, y, 1)

    plt.plot(s_x, y)
    plt.plot(s_x, m*s_x+b)
    plt.xlabel("sqrt(Steps)")
    plt.ylabel("CFG Edit Distance (average of 5)")
    plt.title("Simplified CFG Edit Distance vs sqrt(Steps)")
    plt.show()

def main():

    s = random.randbytes(5)
    #s = b'\x93e\x0c\xb9\xf3'
    #s = b'\x1e\xf8\xfdlp'
    print(s)
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

    #render_cfg(build_cfg_from_ast(ast))    

    old_ast = copy.deepcopy(ast)

    #characterize_edit_dist(ast)

    #render_cfg(gen_simplified_cfg(ast))    
    

    #render_cfg(build_cfg_from_ast(ast))
    #render_cfg(gen_simplified_cfg(ast))    

    proc_edit_dist_data()

    generator = c_generator.CGenerator()

    code = generator.visit(ast)
    code = remove_whitespace(code)

    #print("Generated code;\n", code)

    print(compile_c_code(code), compile_and_test(code))
    #show_cfg(ast)

if __name__ == "__main__":
    main()
