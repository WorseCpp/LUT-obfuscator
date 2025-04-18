from pycparser import c_parser, c_ast, c_generator
import graphviz
import re
from collections import Counter


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

    def number_of_nodes(self):
        return self.counter

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
    else:
        return (label_node, [label_node])
    

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
def build_cfg_from_func(func_def, cfg):
    # Build the CFG for a function definition.
    entry = cfg.new_node("Function: " + func_def.decl.name)
    body_entry, body_exits = process_statement(func_def.body, cfg)
    cfg.add_edge(entry, body_entry)
    end_node = cfg.new_node("End of " + func_def.decl.name)
    for node in body_exits:
        cfg.add_edge(node, end_node)
    # Resolve any pending goto statements by connecting them to the function's end node.
    for pending in cfg.pending_gotos.values():
        for goto_node in pending:
            cfg.add_edge(goto_node, end_node)
    cfg.pending_gotos.clear()
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

    
    for _ in range(10):


        # Save a snapshot of the current graph structure.
        old_body = list(cfg.dot.body)
        
        #print(old_body)

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

        #print(_)

        #print(sorted(list(labels.keys())))

        one_parent_child_nodes = []
        # Identify nodes with exactly one parent and one child.
        for node in labels:
            if len(parents.get(node, [])) == 1 and len(children.get(node, [])) == 1:
                one_parent_child_nodes.append(node)

        filters = ["goto ", "Label:", "Empty"]
        remove_set = set()
        for node_id, lbl in labels.items():
            if any(lbl.startswith(f) for f in filters):
                if node_id not in one_parent_child_nodes:
                    continue
                remove_set.add(node_id)

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

        # Identify all goto statement nodes with no incoming edges.
        goto_no_parent = [
            node_id for node_id, lbl in labels.items()
            if lbl.startswith("goto ") and len(parents.get(node_id, [])) == 0
        ]
        # Remove goto_no_parent nodes from the graph.
        filtered = set(allowed_nodes) - set(goto_no_parent)
        new_dot_filtered = graphviz.Digraph(comment="Simplified CFG")
        for nid in filtered:
            new_dot_filtered.node(nid, labels[nid])

        def follow_chain_filtered(node):
            current = node
            while current not in filtered and current in children and len(children[current]) == 1:
                current = children[current][0]
            return current

        for src in filtered:
            for child in children.get(src, []):
                target = follow_chain_filtered(child)
                if target and target in filtered:
                    new_dot_filtered.edge(src, target)
        new_dot = new_dot_filtered

        # Identify labels (nodes whose label starts with "Label:") that have no incoming goto edges.
        labels_no_goto = []
        for node_id, lbl in labels.items():
            if lbl.startswith("Label:"):
                incoming = parents.get(node_id, [])
                
                #if ("N59" in incoming):
                #    print(incoming, node_id)

                if not any(labels[parent].startswith("goto ") for parent in incoming if parent in labels.keys()):
                    labels_no_goto.append(node_id)
        
        for lbl in labels_no_goto:
            if lbl in children and len(children[lbl]) == 1:
                child = children[lbl][0]
                new_edges = []
                for line in new_dot.body:
                    edge_match = re.match(r'\s*(\w+)\s*->\s*(\w+)', line)
                    if edge_match:
                        src, dst = edge_match.groups()
                        if dst == lbl:
                            line = f'    {src} -> {child}'
                    new_edges.append(line)
                new_dot.body = new_edges

        new_body = []
        for line in new_dot.body:
            node_match = re.match(r'\s*(\w+)\s+\[label="([^"]+)"\]', line)
            if node_match:
                node_id = node_match.group(1)
                if node_id in labels_no_goto:
                    continue
            new_body.append(line)
        new_dot.body = new_body

        # Update cfg.dot with the new simplified graph.
        cfg.dot = new_dot

        # Check convergence by comparing the body of the dot graphs.
        if list(cfg.dot.body) == old_body:
            break
    
    for _ in range(10):
        old_body = list(cfg.dot.body)

        # After CFG simplification converges, re-calculate parents from the final graph.
        labels = {}
        parents = {}
        for line in cfg.dot.body:
            node_match = re.match(r'\s*(\w+)\s+\[label="([^"]+)"\]', line)
            if node_match:
                node_id, lbl = node_match.groups()
                labels[node_id] = lbl
            edge_match = re.match(r'\s*(\w+)\s*->\s*(\w+)', line)
            if edge_match:
                src, dst = edge_match.groups()
                parents.setdefault(dst, []).append(src)
        # Ensure every node appears in the parents dictionary.
        for node in labels:
            parents.setdefault(node, [])
        # Identify and print nodes without a parent.
        nodes_without_parent = [node for node, par_list in parents.items() if not par_list]
        #print("Nodes without a parent:", [labels[a] for a in nodes_without_parent])

        # Remove nodes without a parent unless they are function definitions.
        removable = []
        # Identify nodes without a parent that are not function definitions.
        for node in nodes_without_parent:
            if node in labels and not labels[node].startswith("Function:"):
                removable.append(node)

        # Filter out node and edge entries associated with removable nodes.
        new_body = []
        for line in cfg.dot.body:
            node_match = re.match(r'\s*(\w+)\s+\[label="([^"]+)"\]', line)
            edge_match = re.match(r'\s*(\w+)\s*->\s*(\w+)', line)
            if node_match:
                node_id = node_match.group(1)
                if node_id in removable:
                    continue
            if edge_match:
                src, dst = edge_match.groups()
                if src in removable or dst in removable:
                    continue
            new_body.append(line)
        cfg.dot.body = new_body

        if list(cfg.dot.body) == old_body:
            break

    return cfg

def gen_simplified_cfg(ast):
    # Build the full CFG using previously defined build_cfg_from_ast
    cfg = build_cfg_from_ast(ast)
    # Simplify the CFG graph structure.
    return simplify_cfg_graph(cfg)

# "Edit distance" (fake but approximate)
def graph_edit_distance(cfg_one, cfg_two):

    def extract_graph(dot):
        # Extract nodes (dict: node_id -> label) and edges (set of (src, dst) tuples)
        node_pattern = re.compile(r'\s*(\w+)\s+\[label="([^"]+)"\]')
        edge_pattern = re.compile(r'\s*(\w+)\s*->\s*(\w+)')
        nodes = {}
        edges = set()
        for line in dot.body:
            node_match = node_pattern.match(line)
            if node_match:
                node_id, label = node_match.groups()
                nodes[node_id] = label
            edge_match = edge_pattern.match(line)
            if edge_match:
                src, dst = edge_match.groups()
                edges.add((src, dst))
        return nodes, edges

    nodes_one, edges_one = extract_graph(cfg_one.dot)
    nodes_two, edges_two = extract_graph(cfg_two.dot)

    # Compute node edit distance by comparing node label multisets.
    counter_one = Counter(nodes_one.values())
    counter_two = Counter(nodes_two.values())
    common = sum(min(counter_one[label], counter_two[label]) for label in set(counter_one) | set(counter_two))
    node_edit_distance = (sum(counter_one.values()) + sum(counter_two.values()) - 2 * common)

    # Compute edge edit distance as the absolute difference in number of edges.
    edge_edit_distance = abs(len(edges_one) - len(edges_two))

    # Return total graph edit distance.
    return node_edit_distance + edge_edit_distance

    

   