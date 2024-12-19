"""
Implement a function padded_zip which takes a list of lists lists as a positional argument, plus a keyword argument padding, which should be None by default.

The function should return a tuple of tuples where the i-th tuple contains the i-th element from each of the lists contained in lists. If some of the lists in the input are shorter, padding should be used in place of further elements. Note that padded_zip should work no matter how many lists are contained in lists.

The functionality is similar to Python's built-in zip function, however padded_zip should return a tuple of the same length as the longest input list, and it only strictly needs to work on lists of lists.

Use the following template:
"""

def padded_zip(data, filler = None):

    res = []
    for idx in range(max([len(w) for w in data])): 
        pass





# The following example illustrates how the solution may be used:

l1 = [1, 2, 3, 4, 5]
l2 = [1.5, 2.5, 3.5, 4.5]
l3 = ["please", "send", "help"]
print(padded_zip([l1, l2, l3]))
print(padded_zip([l1, l2, l3, l1], "!"))

"""
The code above should produce the following output:

((1, 1.5, 'please'), (2, 2.5, 'send'), (3, 3.5, 'help'), (4, 4.5, None), (5, None, None))
((1, 1.5, 'please', 1), (2, 2.5, 'send', 2), (3, 3.5, 'help', 3), (4, 4.5, '!', 4), (5, '!', '!', 5))
"""