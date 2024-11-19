#!/usr/bin/env python3

# Testcases were provided by a colegue of mine, I couldnt handle the mental task of writing this god forsaken breadcrumb testcases
# Sidenote: Only copy the code down below, I accidentally deleted the signature for the autograding.
# I am sorry for the inconvenience.

from unittest import TestCase
from task.script import move

class MoveTestSuite(TestCase):

    def test_move_right(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "right")
        expected = (
            (
                "#####   ",
                "###    #",
                "#    o##",
                "   #####"
            ),
            ("left", "up")
        )
        self.assertEqual(expected, actual)

    def test_move_up(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "up")
        expected = (
            (
                "#####   ",
                "### o  #",
                "#     ##",
                "   #####"
            ),
            ("down", "left", "right")
        )
        self.assertEqual(expected, actual)

    def test_move_left(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "left")
        expected = (
            (
                "#####   ",
                "###    #",
                "#  o  ##",
                "   #####"
            ),
            ("left", "right", "up")
        )
        self.assertEqual(expected, actual)

    def test_invalid_move(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "down")

    def test_invalid_character(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   ####x"
        )
        with self.assertRaises(Warning):
            move(state, "right")

    def test_inconsistent_line_length(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   ######"
        )
        with self.assertRaises(Warning):
            move(state, "right")

    def test_multiple_players(self):
        state = (
            "#####   ",
            "### o  #",
            "#   o ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "right")

    def test_no_player(self):
        state = (
            "#####   ",
            "###    #",
            "#     ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "right")

    def test_empty_world(self):
        state = ()
        with self.assertRaises(Warning):
            move(state, "right")

    def test_empty_world_with_empty_strings(self):
        state = ("", "", "")
        with self.assertRaises(Warning):
            move(state, "right")

    def test_invalid_direction(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "diagonal")

    def test_no_possible_moves(self):
        state = (
            "####",
            "#o##",
            "####"
        )
        with self.assertRaises(Warning):
            move(state, "right")
    
    def test_right_outta(self):
        state = (
            "### ",
            "## o",
            "####"
        )
        with self.assertRaises(Warning):
            move(state, "right")
    
    def test_left_outta(self):
        state = (
            "####",
            "o ##",
            " ###"
        )
        with self.assertRaises(Warning):
            move(state, "left")
    
    def test_right_outta2(self):
        state = (
            "### ",
            "## o",
            "####"
        )
        with self.assertRaises(Warning):
            move(state, "right")
    
    def test_up_outta(self):
        state = (
            "o###",
            "  ##",
            " ###"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_left_outta2(self):
        state = (
            "### ",
            "o  #",
            "####"
        )
        with self.assertRaises(Warning):
            move(state, "left")
    
    def test_down_outta(self):
        state = (
            "####",
            "  ##",
            "o###"
        )
        with self.assertRaises(Warning):
            move(state, "down")
    