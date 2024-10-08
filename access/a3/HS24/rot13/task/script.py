def rot_n(plain_text, shift_by):
    return ''.join(chr((ord(char) - 65 + shift_by) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift_by) % 26 + 97) if char.islower() else char for char in plain_text)

print(rot_n("abc", 1))

"""
While working on this task, three utilities will make your life easier: Use isalpha to check, 
if a character is alphabetic (e.g., "a".isalpha() is True), 
use ord to get the ASCII code of a string (e.g., ord("a") is 97), 
and use chr to convert an ASCII code to its corresponding string (e.g., chr(97) is "a"). 
Also, note that should you wish to start out with an empty string, it is defined as "".
"""