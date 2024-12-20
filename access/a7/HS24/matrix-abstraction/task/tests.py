#!/usr/bin/env python3

from unittest import TestCase
from task.script import Matrix

class PublicTestSuite(TestCase):

    def test_instantiation(self):
        m = Matrix([[5, 5], [5, 5]])
        self.assertIsInstance(m, Matrix)

    def test_equality(self):
        m = Matrix([[5, 5], [5, 5]])
        t = Matrix([[5, 5], [5, 5]])
        self.assertTrue(m == t)

    def test_hash_equality(self):
        m = Matrix([[5, 5], [5, 5]])
        t = Matrix([[5, 5], [5, 5]])
        self.assertTrue(hash(m) == hash(t))

    def test_dictionary_key(self):
        m = Matrix([[5, 5], [5, 5]])
        t = Matrix([[5, 5], [5, 5]])
        d = {m: "1", t: "2"}
        d.update({m: "3"})
        self.assertEqual(d[m], "3")

    def test_addition(self):
        m = Matrix([[1, 2], [3, 4]])
        t = Matrix([[5, 6], [7, 8]])
        result = m + t
        expected = Matrix([[6, 8], [10, 12]])
        self.assertTrue(result == expected)

    def test_multiplication(self):
        m = Matrix([[1, 2], [3, 4]])
        t = Matrix([[2, 0], [1, 2]])
        result = m * t
        expected = Matrix([[4, 4], [10, 8]])
        self.assertTrue(result == expected)

    def test_invalid_instantiation(self):
        with self.assertRaises(AssertionError):
            Matrix([[]])
        with self.assertRaises(AssertionError):
            Matrix([[1, 2], [3]])
        with self.assertRaises(AssertionError):
            Matrix([[1, 2], [3, 'a']])
        with self.assertRaises(AssertionError):
            Matrix("invalid")

