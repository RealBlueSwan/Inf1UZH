#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def compress(data):
    if len(data) == 0:
        return((), [])

    # keys in tuple
    keys = tuple(sorted(data[0].keys()))
    
    values = []
    for e in data:
        # a list of tuples
        v = []
        for k in keys:
            v.append(e[k])
        values.append(tuple(v))

    return (keys, values)

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
data = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "c": 6, "b": 5}
]
print(compress(data))