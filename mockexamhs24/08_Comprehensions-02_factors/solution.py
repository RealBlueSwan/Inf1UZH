#!/usr/bin/env python3

def divisor_finder(numbers, potential_divisors):
    return {num: [d for d in potential_divisors if num % d == 0] for num in numbers}

# examples
print(divisor_finder([12], [2, 3, 4, 5]))
print(divisor_finder([12, 14, 16], [2, 3, 4]))
print(divisor_finder([30, 42, 70], [2, 3, 5, 7]))


