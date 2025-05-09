from qol import *
import ast

from CFG import *

import math
import re

def simplify_ast(ast):
    # Recursively process AST nodes to replace if(1) with their true branch
    def simplify_node(node):
        # If the node has nested block_items, simplify them too.
        if hasattr(node, "block_items") and node.block_items is not None:
            node.block_items = simplify_block(node.block_items)
        # For If nodes, simplify any direct children.
        if isinstance(node, c_ast.If):
            if node.iftrue:
                node.iftrue = simplify_node(node.iftrue)
            if node.iffalse:
                node.iffalse = simplify_node(node.iffalse)
        return node

    def simplify_block(block_items):
        new_block = []
        for stmt in block_items:
            # Check if this is an if statement with constant condition "1"
            if (isinstance(stmt, c_ast.If) and isinstance(stmt.cond, c_ast.Constant) and
                    stmt.cond.type == "int" and stmt.cond.value == "1"):
                # Replace the if-statement with its true branch if available.
                if stmt.iftrue:
                    if isinstance(stmt.iftrue, c_ast.Compound) and stmt.iftrue.block_items:
                        new_block.extend(simplify_block(stmt.iftrue.block_items))
                    else:
                        new_block.append(simplify_node(stmt.iftrue))
                # Ignore the false branch; it is unreachable.
            else:
                new_block.append(simplify_node(stmt))
        return new_block

    # Process all function definitions and other top-level nodes.
    for node in ast.ext:
        if isinstance(node, c_ast.FuncDef):
            if node.body and getattr(node.body, "block_items", None):
                node.body.block_items = simplify_block(node.body.block_items)
        else:
            simplify_node(node)

    def remove_assign_42_nodes(node):
        if hasattr(node, "block_items") and node.block_items is not None:
            new_items = []
            for stmt in node.block_items:
                # Skip assignments that solely assign 42 to a variable
                if (isinstance(stmt, c_ast.Assignment) and
                    isinstance(stmt.rvalue, c_ast.Constant) and
                    stmt.rvalue.value == "42"):
                    continue
                new_items.append(remove_assign_42_nodes(stmt))
            node.block_items = new_items
        if isinstance(node, c_ast.If):
            if node.iftrue:
                node.iftrue = remove_assign_42_nodes(node.iftrue)
            if node.iffalse:
                node.iffalse = remove_assign_42_nodes(node.iffalse)
        return node

    for i, top_node in enumerate(ast.ext):
        # Process function definitions specially if they have a compound body.
        if isinstance(top_node, c_ast.FuncDef) and top_node.body and getattr(top_node.body, "block_items", None):
            top_node.body = remove_assign_42_nodes(top_node.body)
        else:
            ast.ext[i] = remove_assign_42_nodes(top_node)
    
    return ast

def remove_if_ones(ast):
    def process_node(node):
        # Process nested blocks if present.
        if hasattr(node, "block_items") and node.block_items is not None:
            node.block_items = process_block(node.block_items)
        # If an if-statement with constant condition "1" is encountered,
        # replace it with its true branch (if available) and ignore the false branch.
        if isinstance(node, c_ast.If):
            if (isinstance(node.cond, c_ast.Constant) and
                node.cond.type == "int" and node.cond.value == "1"):
                if node.iftrue:
                    return process_node(node.iftrue)
                else:
                    return None
            # Otherwise, process the children of the if-statement.
            if node.iftrue:
                node.iftrue = process_node(node.iftrue)
            if node.iffalse:
                node.iffalse = process_node(node.iffalse)
        return node

    def process_block(block_items):
        new_block = []
        for stmt in block_items:
            new_stmt = process_node(stmt)
            if new_stmt is None:
                continue
            # If the result is a compound statement with its own block_items, flatten it.
            if isinstance(new_stmt, c_ast.Compound) and new_stmt.block_items:
                new_block.extend(new_stmt.block_items)
            else:
                new_block.append(new_stmt)
        return new_block

    for i, node in enumerate(ast.ext):
        if isinstance(node, c_ast.FuncDef) and node.body and getattr(node.body, "block_items", None):
            node.body.block_items = process_block(node.body.block_items)
        else:
            ast.ext[i] = process_node(node)
    return ast

def score(tree, org_ast):

    tree_cfg = build_cfg_from_ast(simplify_ast(tree))

    org_cfg = simplify_cfg_graph(build_cfg_from_ast(simplify_ast(org_ast)))
    n_cfg = simplify_cfg_graph(tree_cfg)

    node_count = tree_cfg.number_of_nodes()

    node_cut = 250

    if (node_count > node_cut + 20):
        return math.exp(20)

    return 500 + math.exp((node_count - node_cut)) - graph_edit_distance(org_cfg, n_cfg)    

def score_complexity(tree, org_ast):

    generator = c_generator.CGenerator()
    code = generator.visit(remove_if_ones(simplify_ast(tree)))
    open("code.c","w+").write(code)
    score_command = ["complexity", "--score", "--thresh=1", "code.c"]
    result = subprocess.run(score_command, capture_output=True, text=True)
    out = 0
    for line in result.stdout.split("\n"):
        stripped = line.lstrip()
        if stripped and not stripped[0].isdigit():
            continue
        match = re.search(r'\d+', line)
        if match:
            out += int(match.group(0))
        else:
            pass

    return -out + 100000 * (len(code) > 10 * 250)