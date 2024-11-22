#!/usr/bin/env python3

# Change the functions below to determine the powerset of a given set.
def powerset(nums):
    # Remove duplicates from the input list
    nums = list(set(nums))
    
    if not nums:
        return [[]]
    
    first = nums[0]
    rest_powerset = powerset(nums[1:])
    new_subsets = []
    
    for subset in rest_powerset:
        new_subsets.append([first] + subset)
    
    return rest_powerset + new_subsets

# - Ensure that the function removes duplicates if the input list contains any.

# The following lines call the function and print the return
# value to the Console. This way you can check what they do.
test_set = [1, 2, 3]
result = powerset(test_set)
# Example output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# Note that the order of the powerset could differ depending on the implementation.
# Make sure to look at the predefined test and adjust it if so.
print(result)