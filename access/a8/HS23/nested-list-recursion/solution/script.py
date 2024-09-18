#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters.
def analyze(item):
    if item == []:
        return (0, [])
    elif isinstance(item, int) or isinstance(item, float):
        return (item, [item])
    elif isinstance(item, str):
        return (0, [3 * len(item)])
    elif not isinstance(item, list):
        return (0, [item])
    sum_head, head = analyze(item[0])
    if isinstance(item[0], list):
        head = [head]
    sum_tail, tail = analyze(item[1:])
    return (sum_head + sum_tail, head + tail)


# Examples:
print(analyze("bob"))                      # just a string
print(analyze(3.5))                        # just a number
print(analyze({1: print}))                 # just an arbitrary value
print(analyze(["bob", "alice"]))                    # list with just a string
print(analyze([1, 3, 5]))                  # list with just numbers
print(analyze([1, [6.1, 1], 2.5, "s"]))    # mixed numbers and strings
print(analyze([[["bob", 7], []], 3]))
print(analyze([1, [{}, 2], print, "hi"]))  # including other types
