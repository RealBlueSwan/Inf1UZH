Implement a function `analyze` that takes a parameter `item`, which can be of arbitrary type.
The function will need to exhibit different behavior depending on `item`'s type. In particular,
if `item` is a list, then `analyze` will need to recursively analyze all values in the list according to the following specification.

In any case, the function has two purposes:

 * computing a sum of all integers and floats given to the function (even in nested lists)
 * transforming any strings within the list or any nested lists within according to the rules below

Thus, the function should always return a tuple with two elements, where the first element is the computed sum of numbers and the second element is a list representing the original input (with string modifications applied).

The transformed list (the second tuple value) is similar to the input nested list except that strings
are replaced by an integer with the value of `3 * the length of the string`.

Objects of other types should be represented unmodified in the second tuple value.

For example: For the input `[1, [2.5, {1: 10}], "asap"]` the return value should be `(3.5, [1, [2.5, {1: 10}], 12])`: all the numbers contained in (potentially nested) lists, i.e., 1 and 2.5, are summed for the first tuple value while
the second tuple value contains the original data structure, however with all strings replaced by integers according to the given formula. The dictionary in the nested lists is ignored for the computation and
is not transformed in the output but simply taken as is.

Carefully study the following examples to understand the behavior of `analyze`:
```
print(analyze("bob"))                      # just a string
# (0, [9])
print(analyze(3.5))                        # just a number
# (3.5, [3.5])
print(analyze({1: print}))                 # just an arbitrary value
# (0, [{1: <built-in function print>}])
print(analyze(["bob", "alice"]))           # list with just strings
# (0, [9, 15])
print(analyze([1, 3, 5]))                  # list with just numbers
# (9, [1, 3, 5])
print(analyze([1, [6.1, 1], 2.5, "s"]))    # mixed numbers, strings and nested lists
# (10.6, [1, [6.1, 1], 2.5, 3])
print(analyze([[["bob", 7], []], 3]))
# (10, [[[9, 7], []], 3])
print(analyze([1, [{}, 2], print, "hi"]))  # mixed with other types
# (3, [1, [{}, 2], <built-in function print>, 6])
```

**Important:** You **must** use recursion to solve this task!

**Important:** You may **not** use comprehensions, generator expressions, or `for` or `while` loops in this task!

**Hint:** To check whether a value is of a given type, use the built-in `isinstance` function. E.g.:

```
some_value = 5
if isinstance(some_value, int):
    print("some_value is an integer")
```

**Hint:** Think about what the base cases can be for this function: clearly, if the function is given an empty list, a float or integer, or something that is not a list, no further recursive calls will be necessary and the function can return a concrete value for the given input. Likewise, if a the given value is a non-empty list, you will need to have recursive calls that take the individual list elements.

**Note:** The provided script defines the signature of the function. Do not
change this signature or the automated grading will fail. Do not use any
global variables. Your solution should be self-contained in the solution function.

