from mutations import *

import copy

import z3

import pcpp
from io import StringIO

from score_ast import *
import pickle

from score_tests import *

# Early applicarion of AI --> MatEng
# Find the stat of interest; compare wrt this?
# Find stats of interest; evaluate wrt this; all behaviors you can compare...
# Code similarity metrics; output
# AST hamming distance
# Compare the control flow
# Explain how it works in the presentation
# Send introductory slides beforehand

def main():
    s = "0x" + random.randbytes(5).hex()
    #s = b'\x93e\x0c\xb9\xf3'
    #s = b'\x1e\xf8\xfdlp'
    print(s)
    random.seed(s)

    init_rand_names()

    # Example C code including control flow constructs.
    c_code = open("sample.c", "r").read()

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

    #old_ast = copy.deepcopy(ast)
    #autocorr_graph_edit_distance(ast)

    #ast = MC_mutate(ast, 1000)

    characterize_score(ast, score)

    #characterize_edit_dist(ast)

    #render_cfg(gen_simplified_cfg(ast))    
    

    #render_cfg(build_cfg_from_ast(ast))
    #render_cfg(gen_simplified_cfg(ast))    



    #proc_edit_dist_data()

    generator = c_generator.CGenerator()

    code = generator.visit(ast)
    code = remove_whitespace(code)

    print("Compilation succeeded:", compile_c_code(code, False), "\nTests passed:", compile_and_test(code))
    #show_cfg(ast)

if __name__ == "__main__":
    main()
