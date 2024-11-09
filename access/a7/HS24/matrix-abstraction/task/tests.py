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
        self.assertEqual(d[t], "3")

    def test_addition(self):
        m = Matrix([[5, 5], [5, 5]])
        t = Matrix([[5, 5], [5, 5]])
        result = m + t
        self.assertEqual(result, Matrix([[10, 10], [10, 10]]))

    def test_multiplication(self):
        m = Matrix([[5, 5], [5, 5]])
        t = Matrix([[5, 5], [5, 5]])
        result = m * t
        self.assertEqual(result, Matrix([[50, 50], [50, 50]]))

