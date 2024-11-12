#!/usr/bin/env python3

def caser(s):
    return s.upper() if len(s) > 5 else s.lower()

# examples
print( caser("Hello") )
print( caser("Bananas") )
print( caser("AbC") )
print( caser("i don't know!") )

