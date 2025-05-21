def get_indent(level):
    return "    " * level

def visit_node_list(visitor, nodes, separator=""):
    return separator.join([visitor.visit(node) for node in nodes if node is not None])
