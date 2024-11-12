#!/usr/bin/env python3

from unittest import TestCase
from task.script import Publication

class PublicTestSuite(TestCase):

    def test_example(self):
        a = Publication(["A"], "B", 1234)
        b = Publication(["A"], "B", 1234)
        self.assertEqual(a, b)

    def test_hash(self):
        a = Publication(["A"], "B", 1234)
        b = Publication(["A"], "B", 1234)
        self.assertEqual(hash(a), hash(b))
        c = Publication(["B"], "C", 2345)
        self.assertNotEqual(hash(a), hash(c))

    def test_comparison(self):
        a = Publication(["A"], "B", 1234)
        b = Publication(["A"], "B", 1234)
        c = Publication(["B"], "C", 2345)
        self.assertTrue(a <= b)
        self.assertTrue(a < c)
        self.assertTrue(c > a)
        self.assertTrue(c >= b)

    def test_immutability(self):
        a = Publication(["A"], "B", 1234)
        with self.assertRaises(AttributeError):
            a.__authors = ["X"]
        with self.assertRaises(AttributeError):
            a.__title = "Y"
        with self.assertRaises(AttributeError):
            a.__year = 5678

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
