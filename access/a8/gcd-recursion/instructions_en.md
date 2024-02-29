Implement a **recursive** function `gcd(a,b)` that returns the greatest common divisor of `a` and `b`:

## Specification
 - The `gcd(a,b)` function should call itself recursively
 - The `gcd(a,b)` function should be able to handle mistakenly entered negative numbers
   by converting them to positives. To achieve this, the `gcd(a,b)` should leverage Python's built-in `abs` function
 - If `a` and `b` are zero, a `ValueError` should be raised
 - If either `a` or `b` is zero, but not both, the absolute value of the parameter which is not zero should be returned
 - `gcd(a,b)` should work in both cases `a < b` and `a > b`

## Hints
 - Break it down into chunks; start with only the recursive task and case a > b
 - Start from the base case of the recursion
 - Think of the step closest before the base case; What is the difference?
 - Writing tests will help you!

**Note:** The provided script defines the signature of the functions. Do not change this
 signature or the automated grading will fail.
