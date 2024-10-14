#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def invert(d):
    result = {}
    for k, v in d.items():
        if v not in result:
            result[v] = []
        result[v].append(k)
    # Sort the lists of keys for each value
    for v in result:
        result[v].sort()
    return result

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(invert({"a":1, "b":1, "c":3})) # should return {1: ["a", "b"], 3: ["c"]}
print(invert({3: 2, 1: 2})) # should return {2: [1, 3]}