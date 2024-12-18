"""
Implement a function padded_dict, which takes a list of distinct, hashable values keys and a list of arbitrary values values. It also takes an optional arbitrary value padding, which shall be None by default.

The function padded_dict should create and return a new dictionary, where the keys are taken from keys and the values are taken from values in corresponding order. If values is shorter than keys, the values for the remaining keys should be set to be padding. If keys is shorter than values, the superfluous values of values can be ignored.

You may assume that padded_dict will only be constructed with parameters that match the description. Make sure you correctly formulate the function signature.

"""
def padded_dict(keylist, valuelist, arbitpad = None):
    new_dict = {}
    for i in range(len(keylist)):
        if i >= len(valuelist):
            new_dict[keylist[i]] = arbitpad
        else:

            new_dict[keylist[i]] = valuelist[i]

    return new_dict

print( padded_dict([1, "b", 3], [55, 66, 77] ) )
print( padded_dict([1, "b", 3], [55] ) )
print( padded_dict([1, "b"], [55, 66, 77] ) )

"""
{1: 55, 'b': 66, 3: 77}
{1: 55, 'b': None, 3: None}
{1: 55, 'b': 66}
"""