import random
from .scope import Scope
from .renaming_utils import get_renamed_globally

def create_meaningless_function(visitor):
    base_name = f"__mrf_sem_base_{len(visitor.generated_meaningless_funcs_code)}"
    func_name = base_name
    if visitor.active_techniques.get("rename"):
        func_name = get_renamed_globally(visitor.global_scope, visitor.global_rename_counters, base_name, "mf")
    else:
        visitor.global_scope.symbols.setdefault(base_name, func_name)

    param_name = f"depth_param_mrf_{len(visitor.generated_meaningless_funcs_code)}"
    param_scope = Scope()
    param_renamed = param_scope.declare(param_name, "pm_") if visitor.active_techniques.get("rename") else param_name

    indent1, indent2 = "    ", "        "
    code = f"int {func_name}(int {param_renamed}) {{\n"
    code += f"{indent1}if ({param_renamed} <= {random.randint(0,1)}) {{\n"
    code += f"{indent2}return {param_renamed} + {random.randint(0,5)};\n"
    code += f"{indent1}}}\n"
    code += f"{indent1}int temp_val = ({param_renamed} * {random.randint(1,3)}) - ({param_renamed} / {random.randint(3,5)});\n"
    code += f"{indent1}return {func_name}({param_renamed} - {random.randint(1,2)}) + (temp_val % {random.randint(4,8)});\n"
    code += "}\n"
    visitor.generated_meaningless_funcs_code.append(code)
    return func_name

def generate_call(visitor):
    if not visitor.generated_meaningless_funcs_code:
        return ""
    names = [fn.split('(')[0].split()[-1] for fn in visitor.generated_meaningless_funcs_code]
    chosen = random.choice(names)
    depth = random.randint(2, 5)
    var_orig = f"__mrf_ret_val_sem_{random.randint(1000,9999)}"
    var_renamed = visitor.current_scope.declare(var_orig, "drv_") if visitor.active_techniques.get("rename") else var_orig
    return f"{visitor.get_indent()}int {var_renamed} = {chosen}({depth});"
