#!/usr/bin/env python3

from unittest import TestCase
from task.script import factorial


class PublicTestSuite(TestCase):

    def test1(self):
         self.assertEqual(120, factorial(5))

    def test_0(self):
         self.assertEqual(1, factorial(0))

