def get_renamed_globally(global_scope, rename_counters, original_name, prefix_key):
    count = rename_counters.get(prefix_key, 0)
    new_name = f"{prefix_key}_{count}"
    rename_counters[prefix_key] = count + 1
    global_scope.symbols[original_name] = new_name
    return new_name
