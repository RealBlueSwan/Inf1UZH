#!/usr/bin/env python3

from unittest import TestCase
from task.script import analyze

class PublicTestSuite(TestCase):

    def test_1(self):
        actual = analyze([1, [6, 1, {}], 2, "s"])
        expected = (10, [1, [6, 1, {}], 2, 3])
        self.assertEqual(expected, actual)
