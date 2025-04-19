from mutations import *

import copy

import z3

import pcpp
from io import StringIO

from score_ast import *
import pickle

from score_tests import *
import math
import random

# Early applicarion of AI --> MatEng
# Find the stat of interest; compare wrt this?
# Find stats of interest; evaluate wrt this; all behaviors you can compare...
# Code similarity metrics; output
# AST hamming distance
# Compare the control flow
# Explain how it works in the presentation
# Send introductory slides beforehand

def greedy(ast, itr = 100):

    ast = clean_and_preprocess(ast)

    org_ast = copy.deepcopy(ast)
    best_ast = copy.deepcopy(ast)
    best_score = score(org_ast, best_ast)

    scores = []
    for _ in range(itr):
        candidate = MC_mutate(copy.deepcopy(best_ast), 10)
        candidate_score = score(candidate, org_ast)
        #print(candidate_score, simplify_cfg_graph(build_cfg_from_ast(candidate)).number_of_nodes())
        scores.append(best_score)
        if candidate_score < best_score:
            best_score = candidate_score
            best_ast = candidate

    return best_ast, best_score, scores

def MC_optimize(ast, iterations=100):

    ast = clean_and_preprocess(ast)

    current_ast = copy.deepcopy(ast)
    org_ast = copy.deepcopy(ast)
    best_ast = copy.deepcopy(ast)
    best_score = score(ast, best_ast)
    current_score = best_score
    scores = []

    for i in range(iterations):
        candidate = MC_mutate(copy.deepcopy(current_ast), 10)
        candidate_score = score(candidate, org_ast)
        
        scores.append(best_score)

        # Update best solution if candidate is better
        if candidate_score < best_score:
            best_score = candidate_score
            best_ast = candidate

        # Calculate acceptance probability
        if candidate_score < current_score:
            acceptance_probability = 1.0
        else:
            acceptance_probability = candidate_score / current_score

        if random.random() < acceptance_probability:
            current_ast = candidate
            current_score = candidate_score

        print(f"Iteration {i+1}: Candidate Score = {candidate_score}")

    return best_ast, best_score, scores


def simulated_annealing_optimize(ast, iterations=100, temp_initial=1.0, temp_decay=0.99):

    ast = clean_and_preprocess(ast)

    current_ast = copy.deepcopy(ast)
    org_ast = copy.deepcopy(ast)
    best_ast = copy.deepcopy(ast)
    best_score = score(ast, best_ast)
    current_score = best_score
    temperature = temp_initial

    scores = []

    for i in range(iterations):
        candidate = MC_mutate(copy.deepcopy(current_ast), 10)
        candidate_score = score(candidate, org_ast)
        
        scores.append(best_score)

        # Update best solution if candidate is better
        if candidate_score < best_score:
            best_score = candidate_score
            best_ast = candidate

        # Calculate acceptance probability
        if candidate_score < current_score:
            acceptance_probability = 1.0
        else:
            acceptance_probability = math.exp((current_score - candidate_score) / temperature)

        if random.random() < acceptance_probability:
            current_ast = candidate
            current_score = candidate_score

        temperature *= temp_decay
        print(f"Iteration {i+1}: Candidate Score = {candidate_score}, Temperature = {temperature}")

    return best_ast, best_score, scores

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

    #characterize_score(ast, score)

    best_ast, mc_score, mc_scores = MC_optimize(ast, 100)

    best_ast, greedy_score, g_scores = greedy(ast, 100)

    print(greedy_score)


    best_ast, annealing_score, sa_scores = simulated_annealing_optimize(ast, 100)

    print(mc_score, annealing_score)

    print(g_scores, mc_scores, sa_scores)

    plt.plot(np.linspace(0, 100, 100), g_scores)
    plt.plot(np.linspace(0, 100, 100), mc_scores)
    plt.plot(np.linspace(0, 100, 100), sa_scores)
    plt.show()
    #characterize_edit_dist(ast)

    #render_cfg(gen_simplified_cfg(ast))    
    

    #render_cfg(build_cfg_from_ast(ast))
    #render_cfg(gen_simplified_cfg(ast))    


    #proc_edit_dist_data()

    generator = c_generator.CGenerator()

    code = generator.visit(best_ast)
    code = remove_whitespace(code)

    print("Compilation succeeded:", compile_c_code(code, False), "\nTests passed:", compile_and_test(code))
    #show_cfg(ast)

if __name__ == "__main__":
    main()
