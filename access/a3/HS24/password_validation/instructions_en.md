A password should contain a variety of characters to make it harder
to guess. You are part of a team that develops a new application,
which requires passwords to satisfy the following rules:

* Has a length of 8-16 chars.
* Only contains the characters a-z, A-Z, digits, or the special characters "+", "-", "*", "/".
* Must contain at least 2 lower case and 2 upper case characters, 2 digits, and 2 special characters.

Implement a function `is_valid` that takes a string as a parameter `password`,
determines whether a given password candidate is valid and returns an appropriate
boolean.

Make sure to refer to the ![string documentation](https://docs.python.org/3/library/stdtypes.html#string-methods) to find suitable methods which can tell you whether a character is upper or lower case, or whether it is a digit.

If you don't know how to proceed, consider that you need to
 1. Count the number of lower case characters
 2. Count the number of upper case characters
 3. Count the number of digits
 4. Count the number of characters thar are considered "special"
 5. Count the total number of characters
 6. Check if the numbers from steps 1 to 4 add up to the total number of characters from step 5 (otherwise it also contains disallowed characters)
 7. Check that the numbers from steps 1 to 5 match the requirements (at least 2 each / between 8-16 total, respectively)
Note that you can do most of these steps using `sum()` and simple list comprehensions. The is no need for any `for` loops.

PS: As a sidenote, it should be mentioned that this is only a programming example. In the real world, password rules like these have limited effectiveness, especially considering that they increase the likelyhood of people just putting their password on a post-it next to the screen. A simple sentence like "i prefer tea over coffee every time!!!" is likely more secure than "Paj1vj!b" and easier to remember. Never implement password rules like this in a real application: [optional reading](https://blog.codinghorror.com/password-rules-are-bullshit/).

