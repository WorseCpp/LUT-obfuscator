from qol import *

import re

def create_binary_op(names, n):
    if (len(names) == 0):
        return c_ast.Constant(type="int", value="0")

    # loosely try to make a real issue
    first = random.choice(names)
    ctr = c_ast.BinaryOp(op = "*", left = first, right = first)

    for i in range(1, n):
        ctr = c_ast.BinaryOp(op = "*", left = ctr, right = c_ast.BinaryOp(op = "+", left = first, right = c_ast.Constant(type="int", value=i)))

    return c_ast.BinaryOp(op="%", left=ctr, right = c_ast.Constant(type="int", value=n))

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
        candidates = []

        def collect_candidates(node):
            if isinstance(node, (c_ast.Assignment, c_ast.If, c_ast.For, c_ast.While, c_ast.Decl, c_ast.BinaryOp)):
                candidates.append(node)
            for _, child in node.children():
                collect_candidates(child)

        for stmt in selected_func.body.block_items:
            collect_candidates(stmt)
        
        if not candidates and not valid_funcs:
            return ast

    # Select a random statement from the candidates.
    selected_stmt = random.choice(candidates)

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
    elif isinstance(selected_stmt, c_ast.BinaryOp):
        to_be_opaquified = selected_stmt
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
    elif isinstance(selected_stmt, c_ast.BinaryOp):
        selected_stmt = c_ast.BinaryOp(op = "+", left = selected_stmt, right = opaque_expr)
    else:
        selected_stmt.rvalue = c_ast.BinaryOp(op = "+", left = selected_stmt.rvalue, right = opaque_expr)

    return ast

def remove_oqaque_clauses(ast):
    
    # Filter functions that have a body with statements.
    valid_funcs = [f for f in ast.ext if hasattr(f, "body") and f.body and getattr(f.body, "block_items", None)]
    if valid_funcs:
        selected_func = random.choice(valid_funcs)
        candidates = []
        
        def collect_candidates(node):
            if isinstance(node, (c_ast.Assignment, c_ast.If, c_ast.For, c_ast.While, c_ast.Decl, c_ast.BinaryOp)):
                candidates.append(node)
            for _, child in node.children():
                collect_candidates(child)
        
        for stmt in selected_func.body.block_items:
            collect_candidates(stmt)
    else:
        candidates = []

    # Now candidates holds all the statements that could have been operated upon.
    # You can access or process this list as needed.

    print(candidates)
    
    return ast