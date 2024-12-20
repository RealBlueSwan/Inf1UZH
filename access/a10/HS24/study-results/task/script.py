#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def get_average_grade(path):
    if not os.path.exists(path):    # Return `None`, if the file does not exist 
        return None   
    
    with open(path) as f:
        content = f.read()

        grades = []

        for line in content.splitlines():           # split on newlines
            if '#' in line:
                continue
            if not line:
                continue

            row = line.strip().replace(' ', '')     # split on :
            row = row.split(':')
            
            course, grade = str(row[0]), float(row[1])

            grades.append(grade)

        if len(grades) == 0:                        # `0.0` if the file does not contain any grades.
            return 0.0
        
        return sum(grades)/len(grades)


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(get_average_grade("task/my_grades.txt"))

