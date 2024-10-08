#!/usr/bin/env python3

from unittest import TestCase
from task.script import Publication


class PublicTestSuite(TestCase):

    def test_example(self):
        a = Publication(["A"], "B", 1234)
        b = Publication(["A"], "B", 1234)
        self.assertEqual(a, b)



    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
