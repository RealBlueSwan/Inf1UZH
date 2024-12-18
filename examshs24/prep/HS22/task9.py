"""
You are given a correct implementation of a function min_max_mean, which takes a list of numbers as a parameter values and returns a tuple with 3 values representing the minimum, maximum and average value of values.

Write a test suite that can identify faulty implementations exhibiting the following problems:

The minimum value is incorrect
The maximum value is incorrect
The mean value is incorrect
Implement exactly 3 tests. For an implementation exhibiting exactly one of the isolated faults listed above, exactly one test must fail while the other two must pass.

You may want to introduce bugs into min_max_mean to check whether your test suite works correctly.

Submit your entire Test class as given in the template and do not change its name. Do not submit the min_max_mean function.

Use the following template:
"""

def min_max_mean(values):
    from statistics import mean
    return min(values), max(values), mean(values)

from unittest import TestCase

class TestSuite(TestCase):
    def test_minimum(self):  # The minimum value is incorrect
        expected = 1
        actual = min_max_mean([1, 2, 3])
        self.assertEqual(expected, actual[0])

    def test_maximum(self):  # The maximum value is incorrect
        expected = 3
        actual = min_max_mean([1, 2, 3])
        self.assertEqual(expected, actual[1])
    
    def test_mean(self):     # The mean value is incorrect
        expected = 2
        actual = min_max_mean([1, 2, 3])
        self.assertEqual(expected, actual[2])
    
    
