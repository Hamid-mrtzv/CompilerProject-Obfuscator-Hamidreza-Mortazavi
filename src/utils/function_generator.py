import random
from scope import Scope

class MeaninglessFunctionGenerator:
    def __init__(self, active_techniques, global_scope, current_scope):
        self.active_techniques = active_techniques
        self.global_scope = global_scope
        self.current_scope = current_scope
        self.generated_funcs_code = []
        self.global_rename_counters = {"mf": 0}

    def _get_renamed(self, original_name, prefix_key):
        count = self.global_rename_counters.get(prefix_key, 0)
        new_name = f"{prefix_key}_{count}"
        self.global_rename_counters[prefix_key] = count + 1
        self.global_scope.symbols[original_name] = new_name
        return new_name

    def create_function(self):
        base_name = f"__mrf_sem_base_{len(self.generated_funcs_code)}"
        name = base_name
        if self.active_techniques.get("rename"):
            name = self._get_renamed(base_name, "mf")
        else:
            self.global_scope.symbols[base_name] = name

        param_name = f"depth_param_mrf_{len(self.generated_funcs_code)}"
        param_renamed = param_name
        if self.active_techniques.get("rename"):
            param_renamed = Scope().declare(param_name, "pm_")

        func = f"""int {name}(int {param_renamed}) {{
    if ({param_renamed} <= {random.randint(0,1)}) {{
        return {param_renamed} + {random.randint(0,5)};
    }}
    int temp_val = ({param_renamed} * {random.randint(1,3)}) - ({param_renamed} / {random.randint(2,4) + 1});
    return {name}({param_renamed} - {random.randint(1,2)}) + (temp_val % {random.randint(3,7) + 1});
}}""" 
        self.generated_funcs_code.append(func)
        return name

    def generate_call(self, indent):
        if not self.generated_funcs_code:
            return ""
 
        names = [line.split("(")[0].split()[-1]
                 for line in self.generated_funcs_code if '(' in line and ' ' in line.split('(')[0]]

        if not names:
            return ""

        name = random.choice(names)
        depth = random.randint(2, 5)
        dummy_var = f"__mrf_ret_val_sem_{random.randint(1000,9999)}"
        renamed_var = dummy_var

        if self.active_techniques.get("rename"):
            renamed_var = self.current_scope.declare(dummy_var, "drv_")
        else:
            self.current_scope.symbols[dummy_var] = dummy_var

        return f"{indent}int {renamed_var} = {name}({depth});"
