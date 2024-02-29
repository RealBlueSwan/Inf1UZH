#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def compress(data):
    #extract all the keys
    keys = []
    list1 = []
    list2 = []
    for item in data:
        for key in item:
            keys.append(key)
    keys = tuple(sorted(set(keys)))  # Sort the keys alphabetically

    #cycle throughe every key in keys
    for key in keys:
        #now devide data into two lists and append list1&2 with the values
        list1.append(data[0][key])
        list2.append(data[1][key])
    values = [tuple(list1), tuple(list2)]
    sorted_data = (keys, values)

    return sorted_data

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
data = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "c": 6, "b": 5}
]

print(compress(data))