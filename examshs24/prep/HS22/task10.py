"""
You are given a correct implementation of a function count_booleans, which takes a list of booleans as a parameter booleans and returns a tuple with 3 values: the number of Trues, the number of Falses and the total number of values in booleans.

Write a test suite that can identify faulty implementations exhibiting the following problems:

The number of Trues is incorrect
The number of Falses is incorrect
The total number of elements is incorrect
Implement exactly 3 tests. For an implementation exhibiting exactly one of the isolated faults listed above, exactly one test must fail while the other two must pass.

You may want to introduce bugs into count_booleans to check whether your test suite works correctly.

Submit your entire Test class as given in the template and do not change its name. Do not submit the count_booleans function.

Use the following template:
"""

def count_booleans(booleans):
    return booleans.count(True), booleans.count(False), len(booleans)

from unittest import TestCase

class TestSuite(TestCase):
    def test_number_of_Trues(self):         # The number of Trues is incorrect
        expected = 4
        actual = count_booleans([True, True, False, True, True])
        self.assertEqual(expected, actual[0])

    def test_number_of_Falses(self):        # The number of Falses is incorrect
        expected = 1
        actual = count_booleans([True, True, False, True, True])
        self.assertEqual(expected, actual[1])

    def test_number_of_elements(self):      # The total number of elements is incorrect
        expected = 5
        actual = count_booleans([True, True, False, True, True])
        self.assertEqual(expected, actual[2])
    