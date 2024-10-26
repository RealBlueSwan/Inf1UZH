#!/usr/bin/env python3

# As mentioned in the hints, you might want to use the math package
import math

# perform the Sieve of Eratosthenes algorithm and return all primes <= n
def sieve_of_eratosthenes(n):
    primes_up_to_n = []

    if n < 2:
        return primes_up_to_n
    
    prime = [True for i in range(n+1)]

    prime[0] = False
    prime[1] = False

    p = 2

    while (p*p <= n):
        if prime[p] == True:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    
    
    for idx in range(n+1):                  # Now we convert all the True's into numbers 
        if prime[idx] == True:
            primes_up_to_n.append(idx)
    
    return primes_up_to_n

    """
    - Beware of modifying lists that are you are currently looping over. This can lead to skipped elements, for instance non-primes that remain in the list your function returns.
    - Your implementation should be close to the Sieve of Eratosthenes algorithm, but you may use contains(), remove() etc. on lists which might slow your implementation down.
    - Use math.sqrt() and math.ceil() to find the last integer you need to *sieve*.
    """

    # You don't need to change the following line.
    # It simply returns the list created above.

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(sieve_of_eratosthenes(100))
