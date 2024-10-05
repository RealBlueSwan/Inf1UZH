#!/usr/bin/env python3
from unittest import TestCase

from task import script

class PublicTestSuite(TestCase):

    def test_return_types(self):
        # contains an invalid character, pw should be invalid
        actual = script.is_valid("bbBB22--%")
        self.assertEqual(actual, False)

