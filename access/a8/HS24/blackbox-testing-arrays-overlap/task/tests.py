#!/usr/bin/env python3
from unittest import TestCase
from task.script import sorted_arrays_overlap

# Implement this test suite. Make sure that you define test
# methods and that each method _directly_ includes an assertion
# in the body, or -otherwise- the grading will mark the test
# suite as invalid.


class SortedArraysOverlapTest(TestCase):
    def test_example1(self):        # Checks for right output
        array_1 = [-5, -3, -1, 7, 8, 14, 19]
        array_2 = [-8, -5, -2, -1, 19]
        self.assertEqual(sorted_arrays_overlap(array_1, array_2), [-5, -1, 19])
        
    def test_example2(self):        # Check if its the correct output
        array_1 = [5, 8, 14, 19, 19, 19, 23, 34, 52]
        array_2 = [2, 5, 7, 8, 15, 19, 19, 25, 34, 62]
        self.assertEqual(sorted_arrays_overlap(array_1, array_2), [5, 8, 19, 19, 34])

    def test_returns_list(self):    # Check if result is a list   
        array_1 = [-5, -3, -1, 7, 8, 14, 19]
        array_2 = [-8, -5, -2, -1, 19]
        self.assertIsInstance(sorted_arrays_overlap(array_1, array_2), list)

    def test_returns_empty_lists(self):
        array_1 = [-5, -3, -1, 7, 8, 14, 19]
        array_2 = [2, 3]
        self.assertEqual(sorted_arrays_overlap(array_1, array_2), "There are no overlapping elements in given arrays.")
    
    def test_check_for_empty_lists(self):   # a string `Empty arrays! Neither of the arrays can be empty.` if either of the arguments is an empty list.
        array_1 = []
        array_2 = []
        self.assertEqual(sorted_arrays_overlap(array_1, array_2), "Empty arrays! Neither of the arrays can be empty.")

    def test_not_lists(self):       # a string `Invalid input types! Both parameters should be arrays.` if either of the arguments is not of type `list`.
        array_1 = {}
        array_2 = (1, 2)
        self.assertEqual(sorted_arrays_overlap(array_1, array_2), "Invalid input types! Both parameters should be arrays.")

    def test_invalid_data_types_in_array(self):   # a string `Invalid data types within arrays! Arrays should contain only integers.` if either of the passed lists contains non-integer elements.
        array_1 = [1, "hellothere"]
        array_2 = [2, str]
        self.assertEqual(sorted_arrays_overlap(array_1, array_2), "Invalid data types within arrays! Arrays should contain only integers.")
    
    def test_ascending_order(self): #a string `Not sorted arrays! Both arrays should be sorted in ascending order.` if either of the passed lists is not sorted in ascending order.
        array_1 = [2, 3, 4, 1]
        array_2 = [1, 2, 3, 4]
        self.assertEqual(sorted_arrays_overlap(array_1, array_2), "Not sorted arrays! Both arrays should be sorted in ascending order.")

    def test_identical_elements(self):  # Check if function handles arrays with identical elements correctly
        array_1 = [1, 1, 1, 1]
        array_2 = [1, 1, 1, 1]
        self.assertEqual(sorted_arrays_overlap(array_1, array_2), [1, 1, 1, 1])
