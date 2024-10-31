# Implement a function named venn that takes three lists l1, l2, and l3, each of which contains zero or more values of arbitrary type. 
# The function should return a set containing all those unique values which appear in either l1 or l2 at least once but which do not appear in `l3 .

# You may assume that your function will only be called with parameters that match the given description. 
# Note that the usual equivalence principles apply.

def venn(one, two, three):

    temp_list = []
    for i in one:
        if i is float:
            temp_list.append(int(i))
        else:
            temp_list.append(i)
    temp_list = list(set(temp_list))
    
    for i in two: 
        if i is float:
            temp_list.append(int(i))
        else:
            temp_list.append(i)
    temp_list = list(set(temp_list))

    for i in three:
        if i is float:
            temp_list.remove(int(i))
        else:
            temp_list.remove(i)
    temp_list = list(set(temp_list))
    
    return set(temp_list)


    # don't forget to return the result!

# The following example illustrates how the solution may be used:

print( venn([1, 2, 2, 2, 3, 4], [2, 2, 3, 4], [3]))     # {1, 2, 4}
print( venn([1.0, "hi", 3], [1.0, 3, "hi"], [3, 1]))    # {'hi'}
print( venn([1, 2, 3], [4, 5, 6], []))                  # {1, 2, 3, 4, 5, 6}
print( venn([1, 2, 3], [1, 2, 3], [1, 2, 3]))           # set()