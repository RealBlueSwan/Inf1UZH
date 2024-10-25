#!/usr/bin/env python3


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def min_domino_rotations(top, bottom):
        
    if len(top) != len(bottom) or len(top) == 0 or len(bottom) == 0:    # Check if the lists are of same length, if not return -1
        return -1    
    
    if len(set(top)) == 1 or len(set(bottom)) == 1:                     # Check if there is only one value in top or bottom -> then return 0 
        return 0
    
    needed_value = needed_value_finder(top, bottom)                     # This one is important! returns -1 if there is no common number in all idx
    if needed_value == -1:
        return -1
    
    counter_top = 0
    counter_bottom = 0
    # THIS NEEDS SOME IMPROVEMENT BECAUSE IF BOTTOM AND BOT ARE THE SAME COUNTER STILL INCREASES WHICH IS NOT CORRECT
    for idx in range(len(top)):                                         # Starts at 0, Do a top_swap
        if needed_value == bottom[idx] and needed_value != top[idx]:
            counter_top += 1

    for idx in range(len(bottom)):                                      # Starts at 0, Do a bottom_swap
        if needed_value == top[idx] and needed_value != bottom[idx]:
            counter_bottom += 1
    
    return min(counter_bottom, counter_top)

def needed_value_finder(up, down):
    temp_up = True
    temp_down = True

    for idx in range(len(up)):                                          # Starts at 0
        if up[0] != up[idx] and up[0] != down[idx]:
            temp_up = False
        if down[0] != up[idx] and down[0] != down[idx]:
            temp_down = False

    if temp_up:
        return up[0]
    
    elif temp_down:
        return down[0] 
    
    else:
        return -1


# The following line calls the function which will print # value to the Console.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

print(min_domino_rotations([2, 6, 2, 1, 2, 2], [5, 2, 4, 2, 3, 2]))         # return 2 -> 1 and 3 get swapped
print(min_domino_rotations([3, 5, 1, 2, 6], [3, 6, 3, 3, 6]))               # returns -1 -> no solution
print(min_domino_rotations([3], [3, 6]))                                    # returns -1 -> non equal length
print(min_domino_rotations([1, 2, 1, 1 ], [1, 1, 2, 1]))                    # returns 1 
