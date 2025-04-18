from qol import *
import ast

from CFG import *

import math

def score(tree, org_ast):

    tree_cfg = build_cfg_from_ast(tree)

    org_cfg = simplify_cfg_graph(build_cfg_from_ast(org_ast))
    n_cfg = simplify_cfg_graph(tree_cfg)

    node_count = tree_cfg.number_of_nodes()

    node_cut = 250

    if (node_count > node_cut + 10):
        return math.exp(10)

    return math.exp((node_count - node_cut)) - graph_edit_distance(org_cfg, n_cfg)