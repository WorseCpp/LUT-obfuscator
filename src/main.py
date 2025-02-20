from pycparser import c_parser
import graphviz

def add_nodes_edges(node, dot, parent_id=None):
    """
    Recursively traverse the AST node and add nodes and edges to the graphviz Digraph.
    """
    # Use the object's id as a unique identifier
    node_id = str(id(node))
    
    # Create a label using the type of the node
    label = node.__class__.__name__
    # Optionally add more attributes if available (for example, function or variable names)
    if hasattr(node, 'name') and node.name:
        label += f": {node.name}"
    if hasattr(node, 'declname') and node.declname:
        label += f": {node.declname}"
    
    dot.node(node_id, label=label)
    if parent_id:
        dot.edge(parent_id, node_id)
    
    # Recursively process all children of the current node
    for child_name, child in node.children():
        add_nodes_edges(child, dot, node_id)

def main():
    # Example C code to parse
    c_code = """
    int add(int a, int b) {
        return a * a + b;
    }

    int main() {
        int result = add(10, 20);
        return result;
    }
    """
    
    # Parse the C code using pycparser
    parser = c_parser.CParser()
    ast = parser.parse(c_code)
    
    # Create a Graphviz Digraph to build the AST visualization
    dot = graphviz.Digraph(comment="C AST")
    add_nodes_edges(ast, dot)
    
    # Render the graph to a file (this will create "c_ast.png") and open it with the default viewer
    dot.render("c_ast", format="png", view=True)

if __name__ == "__main__":
    main()
