import random
from .meaningless_func_generator import generate_call

def generate_dead_code(visitor):
    if visitor.active_techniques.get("meaningless_funcs") and visitor.generated_meaningless_funcs_code and random.random() < 0.4:
        call = generate_call(visitor)
        if call: return call
    name = f"dead_v_{visitor.var_name_counter_for_dead_code}"
    visitor.var_name_counter_for_dead_code += 1
    return f"{visitor.get_indent()}int {name} = {random.randint(1000, 9999)};"
