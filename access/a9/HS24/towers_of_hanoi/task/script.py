#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def req_steps(num_disks):
    # implement this function

    # Basecase is when there are no more steps to make and num_discs goes down to 0
    if num_disks == 0:
        return 0
    
    # Shift ‘N-1’ disks from ‘A’ to ‘B’, using C.
    # Shift last disk from ‘A’ to ‘C’.
    # Shift ‘N-1’ disks from ‘B’ to ‘C’, using A.

    # Calls itself twice increases operations exponentially siehe pascals triangle

    return 1 + req_steps(num_disks - 1) + req_steps(num_disks - 1)


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print("For moving {} disks, {} steps are required.".format(30, req_steps(30)))

