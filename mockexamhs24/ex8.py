def divisor_finder(numbers, potential_divisors):
    return {n :[i for i in potential_divisors if n % i == 0] for n in numbers}


    
     




print(divisor_finder([12], [2, 3, 4, 5]))               # {12: [2, 3, 4]}
print(divisor_finder([12, 14, 16], [2, 3, 4]))          # {12: [2, 3, 4], 14: [2], 16: [2, 4]}
print(divisor_finder([30, 42, 70], [2, 3, 5, 7]))       # {30: [2, 3, 5], 42: [2, 3, 7], 70: [2, 5, 7]}




