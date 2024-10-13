#!/usr/bin/python3

def square_numbers(numbers):
    '''this one just serves as an example'''
    return [ number ** 2 for number in numbers ]

def even_numbers(numbers):
    return [ number for number in numbers if number % 2 == 0 ]

def all_even(numbers):
    return [ round(number / 2) * 2 if isinstance(number, float) else (number if number % 2 == 0 else number + 1) for number in numbers ]

def only_integers(numbers):
    return [ number for number in numbers if type(number) == int]

def only_positive(numbers):
    return [ abs(number) for number in numbers ]

def from_1_to_1000_containing_a(a):
    return [ number for number in range(0, 1001) if str(a) in str(number) ]

def multiple_of_a_and_greater_than_b(numbers, a, b):
    return [ number for number in numbers if number > b and number % a == 0]


# print(square_numbers([1, 2, 3]))
# print(even_numbers([1, 2, 3]))
# print(all_even([1, 2, 3]))
# print(only_integers([1.1, 2]))
# print(only_positive([1, -2, -3]))
# print(from_1_to_1000_containing_a(0))
# print(multiple_of_a_and_greater_than_b([1, 4, 6], 2, 3))

