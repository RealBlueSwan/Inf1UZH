#!/usr/bin/env python3
from unittest import TestCase
from task.script import median

# Extend the test suite with regression tests that cover the
# meaningful bug reports. Make sure that you define test methods
# and that each method _directly_ includes an assertion in the
# body, or -otherwise- the grading will mark the test suite as
# invalid.
class MedianTests(TestCase):

    """
    def test_example(self):
        expected = int
        actual = []
        self.assertEqual(median(actual), expected)
    """
    ## insering only one parameter and getting the correct median
    def test_only_one_paramenter(self):
        expected = 1
        actual = [1]
        self.assertEqual(median(actual), expected)

    ## "Average" of the two values that share the middle index. 
    def test_average_of_two_middle_indexes(self):
        expected = 2.5
        actual = [1, 2, 3, 4]
        self.assertEqual(median(actual), expected)

    ## Case where list is empty, but crashing it is often the better option than doing nothing at all... 
    # None coult be a good default but often leads to confusion why it doesnt work, 
    # error handling would be better but I guess in this case its a hint hin on that to do with empty lists. 
    def test_empty_list(self):
        expected = None
        actual = []
        self.assertEqual(median(actual), expected)

    def test_normal_function(self):
        expected = 5
        actual = [1, 5, 10]
        self.assertEqual(median(actual), expected)

    def test_non_sorted_list_median(self):
        expected = 6
        actual = [1, 10, 6]
        self.assertEqual(median(actual), expected)
    
