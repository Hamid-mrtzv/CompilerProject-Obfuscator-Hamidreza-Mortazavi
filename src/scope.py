class Scope:
    def __init__(self, parent=None):
        self.parent = parent
        self.symbols = {}
        self.prefix_counters = {}

    def declare(self, original_name, prefix="v_"):
        count = self.prefix_counters.get(prefix, 0)
        new_name = f"{prefix}{count}"
        self.prefix_counters[prefix] = count + 1
        self.symbols[original_name] = new_name
        return new_name

    def lookup(self, original_name):
        if original_name in self.symbols:
            return self.symbols[original_name]
        if self.parent:
            return self.parent.lookup(original_name)
        if original_name in ["printf", "scanf"]:
            return original_name
        return original_name
