#!/usr/bin/env python3
from unittest import TestCase
from task.script import evolve, Warning


# You are supposed to develop the functionality in a test-driven way.
# Think about relevant test cases and extend the following test suite
# until all requirements of the description are covered. The test suite
# will be run against various correct and incorrect implementations, so
# make sure that you only test the `evolve` function and stick strictly
# to its defined signature.
#
# Make sure that you define test methods and that each method
# _directly_ includes an assertion in the body, or -otherwise- the
# grading will mark the test suite as invalid.
class EvolveTestSuite(TestCase):

    def test_glider(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        expected = ((
            "--------------",
            "| ###        |",
            "| #          |",
            "|  #         |",
            "|            |",
            "|            |",
            "--------------"
        ), 5)
        actual = evolve(field, 4)
        self.assertEqual(expected, actual)

    def test_only_one_neighbor(self):   # A cell that is populated and has only one neighbor dies of solitude and becomes unpopulated.
        field = (
            "--------------",
            "|     #   #  |",
            "|     #   #  |",
            "|            |",
            "|   #        |",
            "|   #    ##  |",
            "--------------"
        )
        expected = ((
            "--------------",
            "|            |",
            "|            |",
            "|            |",
            "|            |",
            "|            |",
            "--------------"
        ), 0)
        actual = evolve(field, 1)
        self.assertEqual(expected, actual)

    def test_has_no_neighbors(self):    # A cell that is populated and has no populated neighbors dies of solitude and becomes unpopulated.
        field = (
            "--------------",
            "|         #  |",
            "|    #       |",
            "|            |",
            "|            |",
            "|   #    #   |",
            "--------------"
        )
        expected = ((
            "--------------",
            "|            |",
            "|            |",
            "|            |",
            "|            |",
            "|            |",
            "--------------"
        ), 0)
        actual = evolve(field, 1)
        self.assertEqual(expected, actual)

    def test_overpopulation_born(self):      # A cell that is populated and has four or more populated neighbors dies due to overpopulation and becomes unpopulated. & Born
        field = (
            "--------------",
            "|    #       |",
            "|   ###      |",
            "|    #       |",
            "|            |",
            "|            |",
            "--------------"
        )
        expected = ((
            "--------------",
            "|   ###      |",
            "|   # #      |",
            "|   ###      |",
            "|            |",
            "|            |",
            "--------------"
        ), 8)
        actual = evolve(field, 1)
        self.assertEqual(expected, actual)

    def test_stays_alive(self):    # A cell that is populated and has two or three populated neighbors survives and stays populated.
        field = (
            "--------------",
            "|    #       |",
            "|   # #      |",
            "|    #       |",
            "|            |",
            "|            |",
            "--------------"
        )
        expected = ((
            "--------------",
            "|    #       |",
            "|   # #      |",
            "|    #       |",
            "|            |",
            "|            |",
            "--------------"
        ), 4)
        actual = evolve(field, 1)
        self.assertEqual(expected, actual)

    def test_invalid_world_type(self):
        with self.assertRaises(Warning):
            evolve(["invalid", "world"], 1)

    def test_invalid_world_characters(self):
        field = (
            "--------------",
            "|            |",
            "|   ###      |",
            "|   #  @     |",  # Invalid character '@'
            "|    #       |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 1)

    def test_invalid_world_dimensions(self):
        field = (
            "----",
            "|  |",
            "----"
        )
        with self.assertRaises(Warning):
            evolve(field, 1)

    def test_invalid_steps_type(self):
        field = (
            "--------------",
            "|            |",
            "|   ###      |",
            "|   #        |",
            "|    #       |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, "one")

    def test_negative_steps(self):
        field = (
            "--------------",
            "|            |",
            "|   ###      |",
            "|   #        |",
            "|    #       |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, -1)

    def test_empty_world(self):
        field = ()
        with self.assertRaises(Warning):
            evolve(field, 1)

    def test_inconsistent_row_lengths(self):
        field = (
            "--------------",
            "|            |",
            "|   ###      |",
            "|   #       |",  # One character less
            "|    #       |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 1)

    """
    * For cells next to the frame, frame cells are considered unpopulated from the cell's perspective.
    """