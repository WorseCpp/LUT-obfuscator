from score_ast import *
import numpy as np

import matplotlib.pyplot as plt
from mutations import *
import copy
from concurrent.futures import ThreadPoolExecutor

def characterize_edit_distance(ast):
    
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
    plt.ylabel("CFG Edit Distance (average of 10)")
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
    plt.plot(s_x, m*s_x)
    plt.xlabel("sqrt(Steps)")
    plt.ylabel("CFG Edit Distance (average of 10)")
    plt.title("Simplified CFG Edit Distance vs sqrt(Steps)")
    plt.show()



def autocorr_graph_edit_distance(ast, num_iterations=100):

    # Compute a time series of edit distances by iteratively mutating the AST
    distances = []

    ast = clean_and_preprocess(ast)

    current_ast = copy.deepcopy(ast)

    cfg_org = simplify_cfg_graph(build_cfg_from_ast(ast))

    mutated_asts = [MC_mutate(copy.deepcopy(current_ast), 1) for _ in range(num_iterations)]


    for i in range(num_iterations):
        # Apply a single mutation
        
        
        cfg_current = simplify_cfg_graph(build_cfg_from_ast(current_ast))
        cfg_mutated = simplify_cfg_graph(build_cfg_from_ast(mutated_asts[i]))

        distances.append(graph_edit_distance(cfg_mutated, cfg_org) - graph_edit_distance(cfg_current, cfg_org))
        
        # Proceed to the next state
        current_ast = mutated_asts[i]

    distances = np.array(distances)
    mean_val = np.mean(distances)
    normalized = distances - mean_val

    # Compute autocorrelation using full convolution then taking the second half
    autocorr = np.correlate(normalized, normalized, mode="full")
    autocorr = autocorr[autocorr.size // 2:]
    autocorr /= autocorr[0]  # normalize so that autocorr[0] == 1

    print("Mean autocorrelation: ", np.mean(autocorr), "Autocorrelation Stdev: ", np.std(autocorr), "Mean Abs:", np.mean(np.abs(autocorr)))

    # Plot the autocorrelation function
    plt.figure()
    plt.plot(np.arange(len(autocorr)), autocorr, marker="o")
    plt.xlabel("Number of Moves made from Original")
    plt.ylabel("One-Move Autocorrelation")
    plt.title("One-Move Autocorrelation of CFG Edit Distance ")
    plt.show()

    return autocorr

def characterize_score(ast, f):
    
    x = list(np.linspace(0, 100, 5)) + list(np.linspace(100, 1000, 5))
    print(x)
    
    old_ast = copy.deepcopy(ast)

    y = []

    for itr in x:

        d = []
        ast = MC_mutate(copy.deepcopy(old_ast), int(itr) + 1)

        y.append(f(ast, old_ast))
        print(y)
        print(build_cfg_from_ast(ast).number_of_nodes())


    plt.plot(x, y)
    plt.xlabel("Steps")
    plt.title("Score of AST vs Steps")
    plt.savefig("fig.png")
    plt.show()