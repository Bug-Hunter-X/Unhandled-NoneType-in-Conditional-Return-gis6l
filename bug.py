def function_with_uncommon_error(a, b):
    if a == 0:
        return b  # This will cause an error if b is None
    return a + b

result = function_with_uncommon_error(0, None)