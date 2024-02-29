#!/usr/bin/env python3

# build a string 
def build_string_pyramid(h):

    # init for h = 0
    s = ""

    # build the first half of the pyramid
    for i in range(1, h + 1):
        for j in range(1,i+1):
            s += str(j)
            if j < i:
                s += "*"
        s += "\n"
    
    # build the second half of the pyramid
    for i in range(h-1, 0, -1):
        for j in range(1,i+1):
            s += str(j)
            if j < i:
                s += "*"
        s += "\n"

    return s

