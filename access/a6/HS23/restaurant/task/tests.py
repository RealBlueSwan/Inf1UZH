#!/usr/bin/env python3

from unittest import TestCase
from task.script import Restaurant, Item, Order


class PublicTestSuite(TestCase):
    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
    def test_get_revenue(self):
        # Create Item objects with name and price
        steak = Item("Steak", 25)
        salad = Item("Salad", 10)
        fish = Item("Fish", 30)
        pizza = Item("Pizza", 40)
        # Create menu
        menu = [steak, salad, fish]
        # Create Restaurant object with name and menu list
        restaurant = Restaurant("Cool Beans", menu)
        # Create list of items to be ordered (note that pizza is not on the menu)
        order = [steak, steak, salad, pizza]
        # Place the order
        restaurant.order(order)
        # Place two more orders
        restaurant.order([steak, steak, steak, salad])
        restaurant.order([salad, pizza])
        # Get the revenue of the restaurant object
        actual = restaurant.get_revenue()
        # Expected return
        expected = 155
        # Assertion
        self.assertEqual(actual, expected)

