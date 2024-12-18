def process(string, needle, mode="remove", character=None):
    if len(needle) < 1:
        raise ValueError
    if mode not in ["remove", "replace"]:
        raise NameError
    if mode == "replace" and character is None:
        raise TypeError
    if mode == "replace":
        return string.replace(needle, character)
    if mode == "remove":
        return string.replace(needle, "")
# examples of how process can be used:
#print( process("abcd_abcd", "b", "remove") )       # acd_acd
#print( process("abcd_abcd", "b", "replace", "*") ) # a*cd_a*cd

from unittest import TestCase
class Tests(TestCase):
    def test_example_file(self):
        actual = process("abcd_abcd", "b", "remove")
        expected = 'acd_acd'
        self.assertEqual(expected, actual)

    def bad_needle(self):
        actual = process("abcd_abcd", "", "remove")
        expected = ValueError
        self.assertEqual(expected, actual)

    def random_mode(self):
        actual = process("abcd_abcd", "b", "blabla")
        expected = TypeError
        self.assertEqual(expected, actual)

    def replace_but_char_none(self):
        actual = process("abcd_abcd", "b", "random", None)
        expected = TypeError
        self.assertEqual(expected, actual)

    