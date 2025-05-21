class IndentationMixin:
    def __init__(self):
        self.indent_level = 0

    def get_indent(self):
        return "    " * self.indent_level

    def visit_node_list(self, nodes, separator=""):
        return separator.join([self.visit(node) for node in nodes if node is not None])
