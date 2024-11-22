#!/usr/bin/env python3
import re

# Change the functions below to determine if the given input is a palindrome.

def is_palindrome(s):

    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()  # Replace everything that isnt a-zA-Z0-9 to '' for cleanup this will enable the further processing

    if len(s) == 0:         # Basecase is when the passed string is empty... potential BUG: when input is already [] then returns True
        return True
    
    if s[0] != s[len(s)-1]: # if first and last char are not same is no palindrom
        return False

    return is_palindrome(s[1:len(s)-1])


# The following lines call the function and prints the return
# value to the Console. This way you can check what it does.
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("No lemon, no melon"))
print(is_palindrome("This is not a palindrome"))
