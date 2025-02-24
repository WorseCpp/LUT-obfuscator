from pycparser import c_parser, c_ast, c_generator
import graphviz

class CFG:
    def __init__(self):
        self.dot = graphviz.Digraph(comment="Control Flow Graph (CFG)")
        self.counter = 0

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