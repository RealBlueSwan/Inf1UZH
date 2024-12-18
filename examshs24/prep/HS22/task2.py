
"""
Implement a function is_perfect_pangram, which takes a string sentence and an optional string alphabet as arguments.

A "pangram" is a word or sentence that uses all letters in an alphabet at least once. A "perfect pangram" uses each letter exactly once.

The function is_perfect_pangram should check if sentence is a perfect pangram for the given alphabet. If no alphabet is given, the 26 letters of the English alphabet should be assumed. Character casing and any characters that are not part of the alphabet should be ignored.

You may assume that is_perfect_pangram will only be constructed with parameters that match the description. Make sure you correctly formulate the function signature.

Use the following template:
"""
import string

def is_perfect_pangram(sentence, alphabet=string.ascii_lowercase):
    sentence = sentence.lower()
    letters = []

    for letter in sentence:
        if letter in alphabet:
            letters.append(letter)

    return len(letters) == len(set(letters)) == len(alphabet)
        


print( is_perfect_pangram("Mr Jock, TV quiz PhD, bags few lynx") )
print( is_perfect_pangram("a b c", "abc") )
print( is_perfect_pangram("azbzc", "abc") )
print( is_perfect_pangram("abc", "abcd") )
print( is_perfect_pangram("abb", "abc") )

"""
True
True
True
False
False
"""