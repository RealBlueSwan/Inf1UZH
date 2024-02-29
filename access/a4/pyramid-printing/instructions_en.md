The goal of this task is to build a string that resembles a pyramid when printed to the console.
The resource folder contains examples for pyramids of different heights.
The image below depicts a pyramid of height h = 5:

![pyramid](resource/height-5-pyramid.png "Pyramid")

Implement a function `build_string_pyramid` that **returns** a string adhering to the specification:

## Specification of the pyramid string:
- the number of lines of the string returned in `build_string_pyramid` should be 2*h -1.
- the h-th line should contain the numbers 1 to n where each number is separated by an asterisk `"*"` (following the pattern `1*2*3*...*h`).
- all other lines should be shorter, decreasing the last/rightmost number by one with each step further away from the h-th line, 
i.e. the line before and after the h-th line both contain the pattern `1*2*3...*h-1`, decreasing until the lines only contain a single `1`.
- h can be assumed non-negative; height 0 should produce the empty string.

## Additional implementation requirements:
- The string must be built within the function `build_string_pyramid`
- This function should **return** the built string (not just print it to the console) as already indicated in the script file.
- The idea is to use `s = ''` as a start and just append to this empty string.
- In this task, you **must** use at least two `for` loops (even though the task could conceivably be solved using comprehensions only).

## Hints:
- use the `range` function and take care of the indices
- use the `"\n"` newline character at the end of every line (including the last)
- concatenating numbers and strings requires the `str()` function
- try to break down the problem into chunks: start by printing the first half of the pyramid and getting it to work before going on to the reverse part.




