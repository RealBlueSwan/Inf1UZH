#!/usr/bin/env python3

def is_valid(password):
    allowed_special = "+-/*"
    count_lower = sum([1 for c in password if c.islower()])
    count_upper = sum([1 for c in password if c.isupper()])
    count_special = sum([1 for c in password if c in allowed_special])
    count_digits = sum([1 for c in password if c.isdigit()])
    length = len(password)
    count_invalid = length - (count_lower + count_upper + count_special + count_digits)

    return (length >= 8
            and count_invalid == 0
            and length <= 16
            and count_lower >= 2
            and count_upper >= 2
            and count_digits >= 2
            and count_special >= 2)
