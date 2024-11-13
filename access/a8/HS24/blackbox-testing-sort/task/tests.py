#!/usr/bin/env python3
from unittest import TestCase
from task.script import sort

class SortTests(TestCase):

    def test_function(self):
        actual = sort([1, 3, 2])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_comparable1(self):
        with self.assertRaises(TypeError):
            sort(["hello", 2])

    def test_comparable2(self):
        actual = sort([2, 1.00])
        expected = [1.00, 2]
        self.assertEqual(actual, expected)

    def test_doesnt_change_original_value(self):
        original = [2, 1]
        sort(original)
        self.assertEqual(original, [2, 1])

    def test_ascending_order_only(self):
        actual = sort([3, 2, 1])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_if_None(self):
        actual = sort(None)
        expected = None
        self.assertEqual(actual, expected)

    def test_if_non_iterable(self):
        actual = sort(1)
        expected = None
        self.assertEqual(actual, expected)

    def test_empty_list(self):
        actual = sort([])
        expected = []
        self.assertEqual(actual, expected)

    def test_single_element(self):
        actual = sort([1])
        expected = [1]
        self.assertEqual(actual, expected)

    def test_strings(self):
        actual = sort(["banana", "apple", "cherry"])
        expected = ["apple", "banana", "cherry"]
        self.assertEqual(actual, expected)

    def test_floats(self):
        actual = sort([3.1, 2.2, 1.3])
        expected = [1.3, 2.2, 3.1]
        self.assertEqual(actual, expected)



