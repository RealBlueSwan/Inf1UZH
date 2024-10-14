#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
#!/usr/bin/env python3

def is_prime(n):

    if n <= 1:
        return "1 is the multiplicative identity" if n == 1 else "Number is negative"
    
    if n <= 3:
        return f"{n} is prime" if n > 1 else "1 is the multiplicative identity"
    
    if n % 2 == 0:
        return f"{n} is not a prime number (2 * {n // 2} = {n})"
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return f"{n} is not a prime number ({i} * {n // i} = {n})"
    
    return f"{n} is prime"

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(is_prime(1003))
