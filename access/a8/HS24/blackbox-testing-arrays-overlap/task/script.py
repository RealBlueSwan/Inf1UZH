#!/usr/bin/env python3

# You can implement this function, but you do not have to.
# The grading will only depend on your test suite.
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.

def sorted_arrays_overlap(array_1, array_2): 
	# returns a list with the the elements that are in both lists
	"""
	* These arrays are non-empty lists of any integers sorted in ascending order.
	* Arrays may have different length and may have duplicate elements.
	"""
	
	if type(array_1) is not list or type(array_2) is not list:	# a string `Invalid input types! Both parameters should be arrays.` if either of the arguments is not of type `list`.
		return "Invalid input types! Both parameters should be arrays."
	
	if not array_1 or not array_2:	# a string `Empty arrays! Neither of the arrays can be empty.` if either of the arguments is an empty list.
		return "Empty arrays! Neither of the arrays can be empty."
	
	for k in array_2:
		if type(k) is not int:
			return "Invalid data types within arrays! Arrays should contain only integers."
	for k in array_1:
		if type(k) is not int:
			return "Invalid data types within arrays! Arrays should contain only integers."
		
	if not (all(array_1[i] <= array_1[i + 1] for i in range(len(array_1) - 1))):
		return "Not sorted arrays! Both arrays should be sorted in ascending order."
	
	if not (all(array_2[i] <= array_2[i + 1] for i in range(len(array_2) - 1))):
		return "Not sorted arrays! Both arrays should be sorted in ascending order."
	


	result = []
	for k in array_1:
		if k in array_2:
			array_2.remove(k)
			result.append(k)

	if result == []:
		return "There are no overlapping elements in given arrays."
	
	return result
