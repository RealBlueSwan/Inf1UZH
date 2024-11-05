def div_sums(numbers, divisors):
    return [sum(i for i in numbers if i % k == 0) for k in divisors ]
    #{x: {y: "larger" if y > x  else "smaller" for y in numbers if x != y}for x in numbers}


print(div_sums([3, 1, 2, 6, 1, 9], [3, 2])) # [3+6+9, 2+6] = [18, 8]
print(div_sums([4, 4, 8], [2, 3]))          # [4+4+8, _] = [16, 0] (no numbers divisble by 3)
