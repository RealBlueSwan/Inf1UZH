from math import pi
number_list = [-1, 1, 2, 3]

def square_root_dict(numbers: [int]):
    return {x: x**0.5 for x in numbers}

def even_odd_dict(numbers: [int]):
    return {x: "even" if x % 2 == 0 else "odd" for x in numbers}

def area_dict(numbers: [int]):
    return {x: {"square": x*x, "circle": '{:.4f}'.format((x**2)* pi)} for x in numbers if x >= 0}
"""
# Expected return value:
{
    1: {
        'square': 1,
        'circle': 3.1415
    },
    2: {
        'square': 4,
        'circle': 12.566
    },
    3: {
        'square': 9,
        'circle': 28.2735
    },
}
!!!The area_dict function does not return a dictionary with the right values. Check your output format.!!!
"""

def smaller_larger_dict(numbers: [int]):
    return {x: {y: "larger" if y > x  else "smaller" for y in numbers if x != y}for x in numbers}


# print(square_root_dict(number_list))
# print(even_odd_dict(number_list))
print(area_dict(number_list))
# print(smaller_larger_dict(number_list))
