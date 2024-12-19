"""
Implement a function merge_dicts which takes a list of dictionaries dicts as a positional argument, plus a keyword argument reverse_priority, which should be False by default.

The function should return a dictionary resulting from merging all the dictionaries in dicts. In other words, the resulting dictionary should contain all items of all dictionaries in dicts. If multiple dictionaries in dicts contain the same key, then the value contained in the last dictionary containing that key (in terms of order within dicts) should take precedence, unless reverse_priority is True, in which case, the first dictionary containing that key should be used.

Note that merge_dicts should work no matter how many dictionaries are contained in dicts.

Use the following template:
"""
def merge_dicts(list1, reverse_priority = False):
    x = {}
    if reverse_priority == False:
        for dict in list1:
            z = dict.copy()   # start with keys and values of x
            x.update(z)    # modifies z with keys and values of y
        return x
    
    rev = list1[::-1]
    for dict in rev:
        z = dict.copy()   # start with keys and values of x
        x.update(z)    # modifies z with keys and values of y
    return x
    
# The following example illustrates how the solution may be used:

d1 = {1: "a", 2: "b", 3: "c"}
d2 = {1: 1, 20: 2, 300: 3}
d3 = {1: "please", 2: "send", 300: "help"}
print(merge_dicts([d1, d2, d3]))
print(merge_dicts([d1, d2, d3], True))

"""
The code above should produce the following output:

{1: 'please', 2: 'send', 3: 'c', 20: 2, 300: 'help'}
{1: 'a', 2: 'b', 300: 3, 20: 2, 3: 'c'}
"""