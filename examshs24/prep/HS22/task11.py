"""
You are given a correct implementation of a function unique_sorted, which takes a list as a parameter values and returns a list containing all unique elements from values in descending order.

Write a test suite that can identify faulty implementations exhibiting the following problems:

An implementation that doesn't work correctly when given an empty list, but works correctly otherwise
An implementation that sorts the result, but does not remove duplicate values
An implementation that does remove duplicates, but does not sort the result
Implement exactly 3 tests. For an implementation exhibiting exactly one of the isolated faults listed above, exactly one test must fail while the other two must pass.

You may want to introduce bugs into unique_sorted to check whether your test suite works correctly.

Submit your entire Test class as given in the template and do not change its name. Do not submit the unique_sorted function.

Use the following template:
"""

def unique_sorted(values):
    return list(sorted(set(values), reverse=True))

from unittest import TestCase

class TestSuite(TestCase):

    def test_empty_list(self):          # An implementation that doesn't work correctly when given an empty list, but works correctly otherwise
        actual = unique_sorted([])
        expected = []
        self.assertEqual(expected, actual)
        
    def test_sorts_removesdupli(self):  # An implementation that sorts the result, but does not remove duplicate values
        actual = unique_sorted([2, 3, 1])
        self.assertEqual(sorted(actual, reverse=True), actual)

    def test_remove_dupli_not_sorted(self):  # An implementation that does remove duplicates, but does not sort the result
        actual = unique_sorted([1,1,2,3,3])
        self.assertEqual(len(actual) == 3)

        