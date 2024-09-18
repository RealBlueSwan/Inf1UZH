#!/usr/bin/env python3
from unittest import TestCase
from script import Inventory


class PublicTestSuite(TestCase):

    def test_example(self):
        inv = Inventory("Test player name", max_weight=300)
        # put an item into the inventory with collect
        inv.collect(("butter knife", 2, 1))
        self.assertEqual(1, len(inv))
        # drop the item
        item = inv.drop(("butter knife", 2, 1))
        self.assertEqual(0, len(inv))
        # is it the right item?
        self.assertEqual(("butter knife", 2, 1), item)

