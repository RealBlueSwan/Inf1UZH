#!/usr/bin/env python3

def gcd(a, b):
    # handle zero-division error
    if a == 0 and b == 0:
        raise ValueError
    else:
        if a == 0 or b == 0:
            return abs(a) if a != 0 else abs(b)
        else:
            # ensure input is positive
            a = abs(a)
            b = abs(b)

            # swap values
            if a < b:
                a, b = b, a

            # base case
            if a % b == 0:
                return b

            # recursive case
            return gcd(b, a % b)

