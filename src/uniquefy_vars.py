from qol import *


class FunctionRenamer(c_ast.NodeVisitor):
    def __init__(self):
        self.counter = 1
        self.var_map = {}

    def visit_FuncDef(self, node):
        # Rename parameters.
        # print("Funcdef!!")
        func_type = node.decl.type
        if func_type.args:
            for param in func_type.args.params:
                if isinstance(param, c_ast.Decl):
                    new_name = f"var_{self.counter}"
                    self.var_map[param.name] = new_name
                    param.name = new_name
                    if isinstance(param.type, c_ast.TypeDecl):
                        param.type.declname = new_name

                    if isinstance(param.type, c_ast.ArrayDecl):
                        param.type.type.declname = new_name

                    if isinstance(param.type, c_ast.PtrDecl):
                        param.type.type.declname = new_name
                    
                    self.counter += 1
        # Process the function body.
        self.visit(node.body)

    def visit_Decl(self, node):
        # Rename a local variable declaration if it is not already renamed.
        if isinstance(node.type, c_ast.TypeDecl) and node.name and node.name not in self.var_map:
            new_name = f"var_{self.counter}"
            self.var_map[node.name] = new_name
            node.name = new_name
            node.type.declname = new_name
            self.counter += 1
        self.generic_visit(node)

    def visit_ID(self, node):
        # Replace identifier usage with its new unique name.
        if node.name in self.var_map:
            node.name = self.var_map[node.name]

def unique_locals(ast):
    # Process each function definition independently.
    renamer = FunctionRenamer()
    renamer.visit(ast)
    return ast