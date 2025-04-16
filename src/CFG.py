from pycparser import c_parser, c_ast, c_generator
import graphviz
import re


class CFG:
    def __init__(self):
        self.dot = graphviz.Digraph(comment="Control Flow Graph (CFG)")
        self.counter = 0
        self.label_nodes = {}
        self.pending_gotos = {}

    def new_node(self, label):
        node_id = f"N{self.counter}"
        self.counter += 1
        self.dot.node(node_id, label)
        return node_id

    def add_edge(self, from_node, to_node):
        self.dot.edge(from_node, to_node)

def gen_code(node):
    # Generate C code from a pycparser AST node for clearer labels.
    generator = c_generator.CGenerator()
    return generator.visit(node)

def process_statement(stmt, cfg):
    # Return a tuple (entry_node, list_of_exit_nodes) for the statement.
    if isinstance(stmt, c_ast.Compound):
        return process_compound(stmt, cfg)
    elif isinstance(stmt, c_ast.If):
        return process_if(stmt, cfg)
    elif isinstance(stmt, c_ast.While):
        return process_while(stmt, cfg)
    elif isinstance(stmt, c_ast.For):
        return process_for(stmt, cfg)
    elif isinstance(stmt, c_ast.Goto):
        return process_goto(stmt, cfg)
    elif isinstance(stmt, c_ast.Label):
        return process_label(stmt, cfg)
    elif isinstance(stmt, c_ast.Return):
        label = "return " + (gen_code(stmt.expr) if stmt.expr else "")
        node = cfg.new_node(label)
        return (node, [])
    else:
        # For simple statements (e.g. assignments, declarations), create a single node.
        node = cfg.new_node(gen_code(stmt))
        return (node, [node])

def process_compound(compound, cfg):
    # Process a compound statement (a block) sequentially.
    entry = None
    exits = []
    if compound.block_items:
        for stmt in compound.block_items:
            stmt_entry, stmt_exits = process_statement(stmt, cfg)
            if entry is None:
                entry = stmt_entry
            # Connect previous statement exits to the current statement entry.
            for prev in exits:
                cfg.add_edge(prev, stmt_entry)
            exits = stmt_exits
        return (entry, exits)
    else:
        # If the block is empty, create an empty node.
        node = cfg.new_node("Empty")
        return (node, [node])
def process_label(label_stmt, cfg):
    # Create a node for the label.
    label_node = cfg.new_node("Label: " + label_stmt.name)
    # Store the label node in a mapping for later goto reference.
    cfg.label_nodes[label_stmt.name] = label_node
    # Connect any pending gotos targeting this label.
    if label_stmt.name in cfg.pending_gotos:
        for goto_node in cfg.pending_gotos[label_stmt.name]:
            cfg.add_edge(goto_node, label_node)
        del cfg.pending_gotos[label_stmt.name]
    # Process the statement following the label.
    if label_stmt.stmt:
        stmt_entry, stmt_exits = process_statement(label_stmt.stmt, cfg)
        cfg.add_edge(label_node, stmt_entry)
        return (label_node, stmt_exits)
def process_goto(goto_stmt, cfg):
    # Create a node for the goto statement.
    goto_node = cfg.new_node("goto " + goto_stmt.name)
    # If the label exists, draw an edge; otherwise, store the goto to link later.
    if goto_stmt.name in cfg.label_nodes:
        target_node = cfg.label_nodes[goto_stmt.name]
        cfg.add_edge(goto_node, target_node)
    else:
        if goto_stmt.name not in cfg.pending_gotos:
            cfg.pending_gotos[goto_stmt.name] = []
        cfg.pending_gotos[goto_stmt.name].append(goto_node)
        cfg.add_edge(goto_node, target_node)
    return (goto_node, [])

def process_if(if_node, cfg):
    # Create a decision node based on the if-statement condition.
    cond_str = "if(" + gen_code(if_node.cond) + ")"
    decision = cfg.new_node(cond_str)
    
    # Process the 'true' branch.
    if if_node.iftrue:
        true_entry, true_exits = process_statement(if_node.iftrue, cfg)
        cfg.add_edge(decision, true_entry)
    else:
        true_exits = [decision]
    
    # Process the 'false' branch if present.
    if if_node.iffalse:
        false_entry, false_exits = process_statement(if_node.iffalse, cfg)
        cfg.add_edge(decision, false_entry)
    else:
        false_exits = [decision]
    
    # Create a join node to merge the two branches.
    join = cfg.new_node("join")
    for node in true_exits + false_exits:
        cfg.add_edge(node, join)
    return (decision, [join])

def process_while(while_node, cfg):
    # Create a node for while condition.
    cond_str = "while(" + gen_code(while_node.cond) + ")"
    decision = cfg.new_node(cond_str)
    
    # Process the loop body.
    if while_node.stmt:
        body_entry, body_exits = process_statement(while_node.stmt, cfg)
        cfg.add_edge(decision, body_entry)
        # Loop back from body exits to condition.
        for node in body_exits:
            cfg.add_edge(node, decision)
    
    # Create an exit node representing exiting the while loop.
    exit_node = cfg.new_node("exit while")
    cfg.add_edge(decision, exit_node)
    return (decision, [exit_node])

def process_for(for_node, cfg):
    # For simplicity, process a for-loop much like a while loop.
    init_str = gen_code(for_node.init) if for_node.init else ""
    cond_str = gen_code(for_node.cond) if for_node.cond else ""
    next_str = gen_code(for_node.next) if for_node.next else ""
    header = f"for({init_str}; {cond_str}; {next_str})"
    decision = cfg.new_node(header)
    
    # Process the loop body.
    if for_node.stmt:
        body_entry, body_exits = process_statement(for_node.stmt, cfg)
        cfg.add_edge(decision, body_entry)
        for node in body_exits:
            cfg.add_edge(node, decision)
    
    exit_node = cfg.new_node("exit for")
    cfg.add_edge(decision, exit_node)
    return (decision, [exit_node])

def build_cfg_from_func(func_def, cfg):
    # Build the CFG for a function definition.
    entry = cfg.new_node("Function: " + func_def.decl.name)
    body_entry, body_exits = process_statement(func_def.body, cfg)
    cfg.add_edge(entry, body_entry)
    end_node = cfg.new_node("End of " + func_def.decl.name)
    for node in body_exits:
        cfg.add_edge(node, end_node)
    return entry

def build_cfg_from_ast(ast):
    
    cfg = CFG()
    
    # Process each function definition in the AST.
    for ext in ast.ext:
        if isinstance(ext, c_ast.FuncDef):
            build_cfg_from_func(ext, cfg)
    
    # Render and view the CFG as a PNG image.
    return cfg


def simplify_cfg_graph(cfg):
    # Build dictionaries to track parents, children, and labels.
    labels = {}
    children = {}
    parents = {}
    
    # Parse nodes and edges from the dot body.
    for line in cfg.dot.body:
        node_match = re.match(r'\s*(\w+)\s+\[label="([^"]+)"\]', line)
        if node_match:
            node_id, lbl = node_match.groups()
            labels[node_id] = lbl
            children.setdefault(node_id, [])
            parents.setdefault(node_id, [])
        edge_match = re.match(r'\s*(\w+)\s*->\s*(\w+)', line)
        if edge_match:
            src, dst = edge_match.groups()
            children.setdefault(src, []).append(dst)
            parents.setdefault(dst, []).append(src)

    one_parent_child_nodes = []
    # Identify nodes with exactly one parent and one child and print their labels.
    for node in labels:
        if len(parents.get(node, [])) == 1 and len(children.get(node, [])) == 1:
            print("Node:", node, "Label:", labels[node])
            one_parent_child_nodes.append(node)

    filters = ["goto ", "Label:", "Empty"]
    remove_set = set()
    for node_id, lbl in labels.items():
        if any(lbl.startswith(f) for f in filters):

            if node_id not in one_parent_child_nodes:
                continue

            remove_set.add(node_id)

    print(remove_set)

    allowed_nodes = set(labels.keys()) - remove_set

    # Create a new simplified graph by combining adjacent remove_set nodes.
    new_dot = graphviz.Digraph(comment="Simplified CFG")
    for node_id in allowed_nodes:
        new_dot.node(node_id, labels[node_id])
    
    def follow_chain(node):
        # Recursively follow the chain through removed nodes until reaching an allowed node.
        current = node
        while current not in allowed_nodes and current in children and len(children[current]) == 1:
            current = children[current][0]
        return current

    # Reconstruct edges among allowed nodes bypassing removed nodes.
    for src in allowed_nodes:
        for child in children.get(src, []):
            target = follow_chain(child)
            if target and target in allowed_nodes:
                new_dot.edge(src, target)
    
    cfg.dot = new_dot
    return cfg

def gen_simplified_cfg(ast):
    # Build the full CFG using previously defined build_cfg_from_ast
    cfg = build_cfg_from_ast(ast)
    # Simplify the CFG graph structure.
    return simplify_cfg_graph(cfg)
