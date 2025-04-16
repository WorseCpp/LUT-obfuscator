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
    return (goto_node, [])
    if hasattr(cfg, "label_nodes") and goto_stmt.name in cfg.label_nodes:
        target_node = cfg.label_nodes[goto_stmt.name]
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

    # Build mappings of incoming and outgoing edges using the dot object's body.
    edges = []
    for line in cfg.dot.body:
        m = re.match(r'\s*(\w+)\s*->\s*(\w+)', line)
        if m:
            edges.append((m.group(1), m.group(2)))

    incoming = {}
    outgoing = {}
    for frm, to in edges:
        outgoing.setdefault(frm, set()).add(to)
        incoming.setdefault(to, set()).add(frm)

    # Identify nodes that have exactly one parent and one child.
    simplifiable_nodes = []
    all_nodes = set(list(incoming.keys()) + list(outgoing.keys()))
    for node in all_nodes:
        if (node in incoming and len(incoming[node]) == 1) and (node in outgoing and len(outgoing[node]) == 1):
            simplifiable_nodes.append(node)

    # For demonstration, print the node IDs that can be simplified.
    for node in simplifiable_nodes:
        print(f"Node {node} can be simplified (one parent and one child).")

    # Iteratively simplify nodes that have exactly one parent and one child.
    changed = True
    edges = []
    for line in cfg.dot.body:
        m = re.match(r'\s*(\w+)\s*->\s*(\w+)', line)
        if m:
            edges.append((m.group(1), m.group(2)))
    while changed:
        changed = False
        incoming = {}
        outgoing = {}
        for frm, to in edges:
            outgoing.setdefault(frm, set()).add(to)
            incoming.setdefault(to, set()).add(frm)
        simplifiable = []
        all_nodes = set(list(incoming.keys()) + list(outgoing.keys()))
        for node in all_nodes:
            if node in incoming and len(incoming[node]) == 1 and node in outgoing and len(outgoing[node]) == 1:
                parent = list(incoming[node])[0]
                child = list(outgoing[node])[0]
                if len(outgoing.get(parent, set())) == 1 and len(incoming.get(child, set())) == 1:
                    simplifiable.append(node)
        if not simplifiable:
            break
        new_edges = []
        # Remove edges that include a simplifiable node.
        for frm, to in edges:
            if frm in simplifiable or to in simplifiable:
                continue
            new_edges.append((frm, to))
        # For every simplifiable node, connect its parent directly to its child.
        for node in simplifiable:
            parent = list(incoming[node])[0]
            child = list(outgoing[node])[0]
            if (parent, child) not in new_edges:
                new_edges.append((parent, child))
            changed = True
        edges = new_edges

    # Rebuild the CFG dot edges with the simplified structure.
    new_body = []
    for line in cfg.dot.body:
        # Preserve non-edge definitions such as node declarations.
        if not re.match(r'\s*\w+\s*->\s*\w+', line):
            new_body.append(line)
    for frm, to in edges:
        new_body.append(f"    {frm} -> {to}")
    #cfg.dot.body = new_body

    # Build a mapping from node IDs to their labels
    node_decl_pattern = re.compile(r'\s*(\w+)\s*\[label="([^"]+)"\]')
    node_labels = {}
    for line in new_body:
        m = node_decl_pattern.match(line)
        if m:
            node_labels[m.group(1)] = m.group(2)

    # Build an adjacency list from the edge definitions
    edge_pattern = re.compile(r'\s*(\w+)\s*->\s*(\w+)')
    adj = {}
    for line in new_body:
        m = edge_pattern.match(line)
        if m:
            frm, to = m.groups()
            adj.setdefault(frm, set()).add(to)

    # Starting from function definition nodes (labels starting with "Function:")
    reachable = set()
    stack = [node for node, label in node_labels.items() if label.startswith("Function:")]
    while stack:
        current = stack.pop()
        if current in reachable:
            continue
        reachable.add(current)
        for child in adj.get(current, []):
            if child not in reachable:
                stack.append(child)

    # Filter out node declarations and edge definitions 
    # to keep only nodes reachable from a function definition.
    cleaned_body = []
    for line in new_body:
        if edge_pattern.match(line):
            m = edge_pattern.match(line)
            frm, to = m.groups()
            if frm in reachable and to in reachable:
                cleaned_body.append(line)
        elif node_decl_pattern.match(line):
            m = node_decl_pattern.match(line)
            if m.group(1) in reachable:
                cleaned_body.append(line)
        else:
            cleaned_body.append(line)
                
    cfg.dot.body = cleaned_body
    
    edge_pattern = re.compile(r'\s*(\w+)\s*->\s*(\w+)')
    node_decl_pattern = re.compile(r'\s*(\w+)\s*\[label="([^"]+)"')
    edge_nodes = set()

    for line in cfg.dot.body:
        m = edge_pattern.search(line)
        if m:
            edge_nodes.add(m.group(1))
            edge_nodes.add(m.group(2))

    new_body = []
    for line in cfg.dot.body:
        m = node_decl_pattern.search(line)
        if m:
            if m.group(1) in edge_nodes:
                new_body.append(line)
        else:
            new_body.append(line)

    cfg.dot.body = new_body

    # Remove node declarations for nodes that are not connected by any edge.
    edge_pattern = re.compile(r'\s*(\w+)\s*->\s*(\w+)')
    connected_nodes = set()
    for line in cfg.dot.body:
        m = edge_pattern.search(line)
        if m:
            connected_nodes.add(m.group(1))
            connected_nodes.add(m.group(2))
    
    node_decl_pattern = re.compile(r'\s*(\w+)\s*\[label="([^"]+)"\]')
    new_body = []
    for line in cfg.dot.body:
        m = node_decl_pattern.match(line)
        if m:
            if m.group(1) in connected_nodes:
                new_body.append(line)
        else:
            new_body.append(line)
    cfg.dot.body = new_body

    return cfg

def gen_simplified_cfg(ast):
    # Build the full CFG using previously defined build_cfg_from_ast
    cfg = build_cfg_from_ast(ast)
    # Simplify the CFG graph structure.
    return simplify_cfg_graph(cfg)
