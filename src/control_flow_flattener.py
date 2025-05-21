import random
from .dead_code_generator import generate_dead_code

def flatten_control_flow(visitor, ctx, stmts):
    state_var_base = "__cff_state_semantic__"
    state_var = visitor.current_scope.declare(state_var_base, "st_") if visitor.active_techniques.get("rename") \
        else f"cff_ctrl_{random.randint(0, 9)}"

    code = [f"{visitor.get_indent()}int {state_var} = 1;"]
    if visitor.active_techniques.get("dead_code"):
        code.append(generate_dead_code(visitor))

    code.append(f"{visitor.get_indent()}while ({state_var} > 0) {{")
    visitor.indent_level += 1
    code.append(f"{visitor.get_indent()}switch ({state_var}) {{")

    for i, stmt in enumerate(stmts):
        code.append(f"{visitor.get_indent()}case {i+1}:")
        visitor.indent_level += 1
        code.append(f"{visitor.get_indent()}{stmt}")
        code.append(f"{visitor.get_indent()}{state_var} = {i+2 if i < len(stmts)-1 else 0};")
        code.append(f"{visitor.get_indent()}break;")
        visitor.indent_level -= 1

    code.append(f"{visitor.get_indent()}default:")
    visitor.indent_level += 1
    code.append(f"{visitor.get_indent()}{state_var} = 0;")
    code.append(f"{visitor.get_indent()}break;")
    visitor.indent_level -= 1
    visitor.indent_level -= 1
    code.append(f"{visitor.get_indent()}}}")
    visitor.indent_level -= 1
    code.append(f"{visitor.get_indent()}}}")

    return code
