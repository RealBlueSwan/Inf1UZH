#!/usr/bin/env python3

def both(f, g, it):
    return (f(it), g(it))

# examples
print( both(str.lower, str.upper, "HeLlO") )
print( both(int, float, "1") )
