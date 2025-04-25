from matplotlib.pyplot import hot
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
import datetime

# Early applicarion of AI --> MatEng
# Find the stat of interest; compare wrt this?
# Find stats of interest; evaluate wrt this; all behaviors you can compare...
# Code similarity metrics; output
# AST hamming distance
# Compare the control flow
# Explain how it works in the presentation
# Send introductory slides beforehand

def greedy(ast, itr = 100, steps = 10):

    ast = clean_and_preprocess(ast)

    org_ast = copy.deepcopy(ast)
    best_ast = copy.deepcopy(ast)
    best_score = score(org_ast, best_ast)

    scores = []
    for _ in tqdm(range(itr)):
        candidate = MC_mutate(copy.deepcopy(best_ast), steps, False)
        candidate_score = score(candidate, org_ast)
        #print(candidate_score, simplify_cfg_graph(build_cfg_from_ast(candidate)).number_of_nodes())
        scores.append(best_score)
        if candidate_score <= best_score:
            best_score = candidate_score
            best_ast = candidate

    return best_ast, best_score, scores

def MC_optimize(ast, iterations=100, steps = 10, scoring = score):

    ast = clean_and_preprocess(ast)

    current_ast = copy.deepcopy(ast)
    org_ast = copy.deepcopy(ast)
    best_ast = copy.deepcopy(ast)
    best_score = scoring(ast, best_ast)
    current_score = best_score
    scores = []

    for i in tqdm(range(iterations)):
        candidate = MC_mutate(copy.deepcopy(current_ast), steps, False)
        candidate_score = scoring(candidate, org_ast)
        
        scores.append(best_score)

        # Update best solution if candidate is better
        if candidate_score < best_score:
            best_score = candidate_score
            best_ast = candidate

        # Calculate acceptance probability
        if candidate_score < current_score:
            acceptance_probability = 1.0
        else:
            if (candidate_score > math.exp(7)):
                acceptance_probability = 0.0
            else:
                acceptance_probability = candidate_score / current_score

        if random.random() < acceptance_probability:
            current_ast = candidate
            current_score = candidate_score

        print(f"Iteration {i+1}: Candidate Score = {candidate_score}")

    return best_ast, best_score, scores


def simulated_annealing_optimize(ast, iterations=100, steps = 10, temp_initial=1.0, temp_decay=0.995, scoring = score):

    ast = clean_and_preprocess(ast)

    current_ast = copy.deepcopy(ast)
    org_ast = copy.deepcopy(ast)
    best_ast = copy.deepcopy(ast)
    best_score = scoring(ast, best_ast)
    current_score = best_score
    temperature = temp_initial

    scores = []

    for i in tqdm(range(iterations)):
        candidate = MC_mutate(copy.deepcopy(current_ast), steps, False)
        candidate_score = scoring(candidate, org_ast)
        
        scores.append(best_score)

        # Update best solution if candidate is better
        if candidate_score < best_score:
            best_score = candidate_score
            best_ast = candidate

        # Calculate acceptance probability
        if candidate_score < current_score:
            acceptance_probability = 1.0
        else:

            if (temperature == 0):
                acceptance_probability = 0
            else:
                if (candidate_score != current_score):
                    print()
                    print("Cand. score, curr score, diff, temp")
                    print(candidate_score, current_score, current_score - candidate_score, temperature)
                    print("Exponent, p_swap")
                    print((current_score - candidate_score) / temperature, math.exp((current_score - candidate_score) / temperature))
                acceptance_probability = math.exp((current_score - candidate_score) / temperature)

        if random.random() < acceptance_probability:
            current_ast = candidate
            current_score = candidate_score

        temperature *= temp_decay
        print(f"Iteration {i+1}: Candidate Score = {candidate_score}, Temperature = {temperature}")

    return best_ast, best_score, scores

def grad_optimization(ast, iterations=100, steps = 10, scoring=score):

    ast = clean_and_preprocess(ast)

    current_ast = copy.deepcopy(ast)
    org_ast = copy.deepcopy(ast)
    best_ast = copy.deepcopy(ast)
    best_score = scoring(ast, best_ast)
    current_score = best_score

    scores = []

    hot_vector = [0 for i in range(8)]

    for i in tqdm(range(iterations)):

        cands = []
        for pos in range(len(hot_vector)):
            
            hot_vector = np.array([0]*8)
            hot_vector[pos] = 1

            candidate = mutate_vector_style(copy.deepcopy(current_ast), 1, False, hot_vector)
            candidate_score = scoring(candidate, org_ast)
            cands.append((candidate, candidate_score))


        best_cand = min(cands, key=lambda k : k[1])

        for i in range(len(hot_vector)):
            if (cands[i] == best_cand):
                print(i)

        if (best_cand[1] <= best_score):
            current_ast = best_cand[0]
            best_score = best_cand[1]
            best_ast = current_ast
        
        scores.append(best_score)

        # Update best solution if candidate is better
       

    return best_ast, best_score, scores

def avg_runs(ast, f, N=100, n_steps=1, r_trials=1, scoring=score, **kwargs):
    gradient_scores = []
    best_ast = copy.deepcopy(ast)
    for i in range(r_trials):
        best_ast, grad_score, grad_scores = f(copy.deepcopy(ast), N, n_steps, scoring=scoring, **kwargs)
        gradient_scores.append(grad_scores)
    gradient_scores = np.array(gradient_scores)
    gradient_scores = [np.mean(gradient_scores[:, i]) for i in range(len(gradient_scores[0]))]

    return gradient_scores, best_ast


def code_to_ast(c_code):
    pp = pcpp.Preprocessor()
    pp.parse(c_code)
    output = StringIO()
    pp.write(output)
    c_code = output.getvalue()

    parser = c_parser.CParser()
    ast = parser.parse(c_code)
    return ast

def main():
    generator = c_generator.CGenerator()
    s = "0x" + random.randbytes(5).hex()
    #s = "0xaecccecdab"
    #s = b'\x93e\x0c\xb9\xf3'
    #s = b'\x1e\xf8\xfdlp'
    print(s)
    random.seed(s)

    init_rand_names()

    # Example C code including control flow constructs.
    c_code = open("sample.c", "r").read()

    ast = code_to_ast(c_code)

    ast = clean_and_preprocess(ast)

    canon_cfg = simplify_cfg_graph(build_cfg_from_ast(simplify_ast(ast)))

    
    N = 1000

    n_steps = 1

    r_trials = 1

    print(score_complexity(code_to_ast(open("code.c","r").read()), ast))

    scoring = score_complexity

    #greedy_scores, greedy_best_ast = avg_runs(ast, greedy, N, n_steps, r_trials)
    #plt.plot(np.linspace(0, len(greedy_scores), len(greedy_scores)), greedy_scores, label=f"Greedy")

    gradient_scores, grad_best_ast = avg_runs(ast, grad_optimization, N, n_steps, r_trials, scoring=scoring)
    plt.plot(np.linspace(0, len(gradient_scores), len(gradient_scores)), gradient_scores, label=f"Gradient")

    t_int = 1.0
    t_dec = round((.001)**(1 / (N*8)), 3)

    simanneal_scores, sa_best_ast = avg_runs(ast, simulated_annealing_optimize, N*8, n_steps, r_trials, scoring=scoring, temp_initial=t_int, temp_decay=t_dec)

    plt.plot(np.linspace(0, len(simanneal_scores) // 8, len(simanneal_scores) // 8), simanneal_scores[::8], label=f"SA scores (T0 = {t_int}, td = {t_dec})")


    filename = datetime.datetime.now().strftime("best_asts_%Y-%m-%d_%H-%M-%S.c")

    grad_cfg = build_cfg_from_ast(simplify_ast(grad_best_ast))
    sa_cfg = build_cfg_from_ast(simplify_ast(sa_best_ast))

    grad_cfg = simplify_cfg_graph(grad_cfg)
    sa_cfg = simplify_cfg_graph(sa_cfg)

    render_cfg(grad_cfg)
    render_cfg(sa_cfg)

    print(graph_edit_distance(grad_cfg, sa_cfg))
    print(graph_edit_distance(grad_cfg, canon_cfg))
    print(graph_edit_distance(canon_cfg, sa_cfg))


    with open(filename, "w+") as f:
        #f.write("greedy_best_ast")
        #f.write(generator.visit(greedy_best_ast))
        f.write("grad_best_ast\n")
        f.write(generator.visit(grad_best_ast))
        f.write("sa_best_ast\n")
        f.write(generator.visit(sa_best_ast))
    print("ASTs saved to best_asts.pkl")

    # Generate a filename with current datetime.
    filename = datetime.datetime.now().strftime("scores_%Y-%m-%d_%H-%M-%S.pkl")
    
    # Prepare a dict with the scores.
    all_scores = {
        #"g_scores": greedy_scores,
        "gradient_scores": gradient_scores,
        "sa_scores": simanneal_scores,  # using the averaged SA scores
        "sa_settings":{"t_int":t_int, "t_dec":t_dec}
    }

    # Save the scores using pickle.
    with open(filename, "wb") as f:
        pickle.dump(all_scores, f)

    print(f"Scores saved to {filename}")

    plt.xlabel("Step Number")
    plt.ylabel("Best Score")
    plt.title(f"Best Score vs Step Number (Avg over {r_trials} Trials)")
    plt.legend(loc='best')
    plt.savefig("figure.png")
    plt.show()
    #characterize_edit_dist(ast)



    # code = generator.visit(best_ast)
    # code = remove_whitespace(code)

    #print("Compilation succeeded:", compile_c_code(code, False), "\nTests passed:", compile_and_test(code))
    #show_cfg(ast)

if __name__ == "__main__":
    main()
