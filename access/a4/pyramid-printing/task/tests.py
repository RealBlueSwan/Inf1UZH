#!/usr/bin/env python3
from unittest import TestCase

from task.script import build_string_pyramid

# This test suite only tests whether the value returned by
# the solution function has the correct type. If this test
# passes, that does not mean that you will get any points.
# The grading system uses different, more exhaustive tests.

# Feel free to extend the class with your own test cases,
# which will then also be executed in every "Test & Run".

class PublicTestSuite(TestCase):

    def test_height_one(self):
        actual = build_string_pyramid(1)
        m = f"For a pyramid of h=1, the string should be '1\n', but it was '{actual}' ."
        self.assertEqual("1\n", actual, m)

