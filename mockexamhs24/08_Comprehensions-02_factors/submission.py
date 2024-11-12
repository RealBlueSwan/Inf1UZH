def divisor_finder(numbers, potential_divisors):
    return {n :[i for i in potential_divisors if n % i == 0] for n in numbers}