#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def merge(a ,b):

    if len(a) == 0 or len(b) == 0:
        return []

    maxlen = max(len(a), len(b))

    cur_a = None
    cur_b = None
    res = []

    for i in range(maxlen):
        if i < len(a):
            cur_a = a[i]
        if i < len(b):
            cur_b = b[i]
        res.append((cur_a, cur_b))

    return res


# Test cases
#print(merge([0, 1, 2], [5, 6, 7]))  # should return [(0, 5), (1, 6), (2, 7)]
#print(merge([2, 1, 0], [5, 6]))     # should return [(2, 5), (1, 6), (0, 6)]
#print(merge([], [2, 3]))            # should return []
#print(merge([1, 2], [3, 4, 5, 6]))  # should return [(1, 3), (2, 4), (2, 5), (2, 6)]
#print(merge([1, 2, 3], [4]))        # should return [(1, 4), (2, 4), (3, 4)]