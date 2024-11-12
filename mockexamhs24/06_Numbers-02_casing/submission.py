def div_sums(numbers, divisors):
    return [sum(i for i in numbers if i % k == 0) for k in divisors ]