#!/usr/bin/env python3

from urllib.parse import quote

def encode(s):
    return quote(s)

# examples
print( encode("/El Niño/") )
print( encode("Hello, world!") )

