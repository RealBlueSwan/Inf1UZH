
#!/usr/bin/env python3
from random import randrange
from math import factorial

# These variables are required for the automatic grading to work, do not change
# their names. You can change values of these variables.
min_length_global = 0
max_length_global = 5
char_start_global = 30
char_end_global = 65


# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def fuzzer(min_length, max_length, char_start, char_end):
    randomstring = ''

    # test if inputs are ok or else raise Warning!
    if min_length > max_length or char_start > char_end:
        raise Warning("Inputs for fuzzer are invalid")

    for _ in range(randrange(min_length, max_length, 1)):
        #adds one string to each iteration
        randomstring = randomstring + chr(randrange(char_start, char_end, 1))
    
    return randomstring

# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def calculate_factorial(inp):

    if inp == None:
        return ('1', "Other error")
    
    if inp.isdigit() == False:
        return ('1', "Other error")

    inp = int(inp)

    if inp < 0:
        return ('1', "ValueError: number negative")
    
    if inp > 10:
        return ('1', "ValueError:number too large")
    
    return ('0', factorial(inp))
    

# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def run(trials):
    #create a list for the task...
    tuplelist = []
    for _ in range(trials):
        tuplelist.append(calculate_factorial(fuzzer(min_length_global, max_length_global, char_start_global, char_end_global)))

    # this function should make use of the other two functions
    # for the input of the fuzzer functions use the global variables
    # this is required else the automatic testing is not working
    return tuplelist

# The following line calls the function run and prints the return
# value to the Console.
print(run(10))
#print(fuzzer(3, 10, 67, 80))
#print(calculate_factorial("3"))