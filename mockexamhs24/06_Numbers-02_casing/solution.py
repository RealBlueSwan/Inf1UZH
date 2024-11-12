#!/usr/bin/env python3

def div_sums(numbers, divisors):
    res = []
    for d in divisors:
        match = [n for n in numbers if n % d == 0]
        res.append(sum(match))
    return res




# examples
print(div_sums([3, 1, 2, 6, 1, 9], [3, 2])) # [3+6+9, 2+6] = [18, 8]
print(div_sums([4, 4, 8], [2, 3]))          # [4+4+8, _] = [16, 0] (no numbers divisble by 3)
