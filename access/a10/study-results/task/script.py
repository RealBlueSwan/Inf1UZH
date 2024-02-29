#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def get_average_grade(path):
    # Sidenote: make sure you always refer to 'path' inside this
    # function, and not to a specific path string directly. Your
    # implementation may be called with different paths.
    if not os.path.exists(path):
        pass # what to do?
    return -1


# The following line calls the function and prints the return
# value to the console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(get_average_grade("task/my_grades.txt"))

