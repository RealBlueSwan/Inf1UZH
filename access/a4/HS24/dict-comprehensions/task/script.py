from math import pi
number_list = [-1, 1, 2, 3]

def square_root_dict(numbers: [int]):
    return {x: x**0.5 for x in numbers}

def even_odd_dict(numbers: [int]):
    return {x: "even" if x % 2 == 0 else "odd" for x in numbers}

def area_dict(numbers: [int]):
    return { x: {"square": x**2, "circle": pi * x**2} for x in numbers if x >= 0 }
    
def smaller_larger_dict(numbers: [int]):
    return {x: {y: "larger" if y > x  else "smaller" for y in numbers if x != y}for x in numbers}


# print(square_root_dict(number_list))
# print(even_odd_dict(number_list))
# print(area_dict(number_list))
# print(smaller_larger_dict(number_list))
