#!/usr/bin/env python3
from unittest import TestCase

from task import script


# This test suite only tests one simple example and whether
# the value returned by the solution function has the correct
# type. If this test passes, it does not mean that you will
# get any points. The grading system uses different, more
# exhaustive tests.

# Feel free to extend the class with your own test cases,
# which will then also be executed in every "Test & Run".


class PublicTestSuite(TestCase):
    def test_correct_return_type(self):
        nested_list = [1, [8, 4], 2, 3]
        actual = script.flatten_list(nested_list)
        self.assertIsInstance(actual, list)

    def test_no_nested_lists_AKABASECASE(self):
        nested_list = [1, 2, 3, 4]  
        actual = script.flatten_list(nested_list)
        expected = [1, 2, 3, 4]
        self.assertEqual(actual, expected)
    
    def test_no_list_input(self):
        not_list = 1
        actual = script.flatten_list(not_list)
        self.assertEqual(actual, TypeError)

    def test_correct_output_1(self):
        nested_list = [1, [2, [3, 4], 5], [6, 7], 8]
        actual = script.flatten_list(nested_list)
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(actual, expected)

    def test_correct_output_2(self):
        nested_list = [[4.5, 6, "string"], "d", "g", ["f", 1, 6, ["another_string"]]]
        actual = script.flatten_list(nested_list)
        expected = [4.5, 6, "string", "d", "g", "f", 1, 6, "another_string"]
        self.assertEqual(actual, expected)

