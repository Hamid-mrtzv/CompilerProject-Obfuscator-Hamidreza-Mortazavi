import random

class DeadCodeGenerator:
    def __init__(self, active_techniques, func_generator):
        self.active_techniques = active_techniques
        self.func_generator = func_generator
        self.counter = 0

    def generate(self, indent):
        if self.active_techniques.get("meaningless_funcs") and self.func_generator.generated_funcs_code and random.random() < 0.4:
            stmt = self.func_generator.generate_call(indent)
            if stmt:
                return stmt

        name = f"dead_v_{self.counter}"
        value = random.randint(1000, 9999)
        self.counter += 1
        return f"{indent}int {name} = {value};"
