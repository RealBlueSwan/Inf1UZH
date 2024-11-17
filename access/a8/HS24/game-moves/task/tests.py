#!/usr/bin/env python3
from unittest import TestCase
from task.script import move

# You are supposed to develop the functionality in a test-driven way.
# Think about relevant test cases and extend the following test suite
# until all requirements of the description are covered. The test suite
# will be run against various correct and incorrect implementations, so
# make sure that you only test the `move` function and stick strictly
# to its defined signature.
#
# Make sure that you define test methods and that each method
# _directly_ includes an assertion in the body, or -otherwise- the
# grading will mark the test suite as invalid.
class MoveTestSuite(TestCase):

    def test_move_right(self):      # Normal right test
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

    def test_move_left(self):       # Normal left test
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
    
    def test_move_up(self):         # Normal up test
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

    def test_no_player_character(self):
        state = (
            "#####",
            "#   #",
            "#   #",
            "#####"
        )
        with self.assertRaises(Warning) as context:
            move(state, "up")
        self.assertEqual(str(context.exception), "no player character found")

    def test_too_many_players(self):
        state = (
            "#####",
            "# o #",
            "# o #",
            "#####"
        )
        with self.assertRaises(Warning) as context:
            move(state, "up")
        self.assertEqual(str(context.exception), "too many players")

    def test_invalid_character(self):
        state = (
            "#####",
            "# x #",
            "# o #",
            "#####"
        )
        with self.assertRaises(Warning, msg="invalid character: x"):
            move(state, "up")

    def test_invalid_character_multiple(self):
        state = (
            "#####",
            "# o #",
            "# x #",
            "# y #",
            "#####"
        )
        with self.assertRaises(Warning, msg="invalid character: x"):
            move(state, "up")

    def test_invalid_character_only(self):
        state = (
            "#####",
            "# x #",
            "#####"
        )
        with self.assertRaises(Warning, msg="invalid character: x"):
            move(state, "up")

    def test_invalid_character_with_hashes(self):
        state = (
            "#####",
            "# o #",
            "# # #",
            "# x #",
            "#####"
        )
        with self.assertRaises(Warning, msg="invalid character: x"):
            move(state, "up")

    def test_invalid_character_with_player(self):
        state = (
            "#####",
            "# o #",
            "# x #",
            "# o #",
            "#####"
        )
        with self.assertRaises(Warning, msg="invalid character: x"):
            move(state, "up")

    def test_invalid_character_with_empty_row(self):
        state = (
            "#####",
            "# o #",
            "#   #",
            "",
            "# x #",
            "#####"
        )
        with self.assertRaises(Warning, msg="The bord has different row dimensions"):
            move(state, "up")

    def test_invalid_character_integer(self):
        state = (
            "#####",
            "# o #",
            "# 4 #",
            "#####"
        )
        with self.assertRaises(Warning, msg="invalid character: 4"):
            move(state, "up")

    def test_unequal_length_strings(self):
        state = (
            "#####",
            "# o #",
            "####",
            "#####"
        )
        with self.assertRaises(Warning, msg="The bord has different row dimensions"):
            move(state, "up")

    def test_invalid_character_symbol(self):
        state = (
            "#####",
            "# o #",
            "# / #",
            "#####"
        )
        with self.assertRaises(Warning, msg="invalid character: /"):
            move(state, "up")

    def test_outside_of_bord(self):
        state = (
            "#####",
            "#   o",
            "#   #",
            "#####"
        )
        with self.assertRaises(Warning, msg="The move is not possible"):
            move(state, "right")

    def test_no_direction_provided(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        with self.assertRaises(Warning, msg="No direction provided"):
            move(state, None)

    def test_move_to_blocked_position(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        with self.assertRaises(Warning, msg="The move is not possible"):
            move(state, "down")

    def test_invalid_direction(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        with self.assertRaises(Warning, msg="The move is not possible"):
            move(state, "diagonal")

    def test_empty_direction(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        with self.assertRaises(Warning, msg="No direction provided"):
            move(state, "")

    def test_non_string_direction(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        with self.assertRaises(Warning, msg="No direction provided"):
            move(state, 123)

    def one_character_check(self, state):  # Moved one_character_check logic here
        counter = 0
        for row in state:
            if len(row) == 0:
                raise Warning("The bord has different row dimensions")
            for character in list(row):
                if character not in (" ", "#", "o"):
                    raise Warning(f"invalid character: {character}")
                if character == "o":
                    counter += 1
        
        if counter == 0:
            raise Warning("no player character found")
        
        if counter > 1:
            raise Warning("too many players")
