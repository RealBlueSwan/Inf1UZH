#!/usr/bin/env python3

# use this list of presumably known Whatsapp numbers to check
# whether a trial nr from the function below exists in Whatsapp.
# Note that the grading framework might use different numbers here.
wa_nrs = ["0781111119", "0792653913", "0797763139", "0792793193", "0781139022", "0764320165"]


# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def get_possible_nrs(n):

    # This function accepts a string n for juliets number where one digit is missing.
    if len(n) != 9:
        raise Exception(f"The provided Number {n} doesnt have 9 digits but {len(n)}!")
    
    # and should return a list of all whatsapp numbers that might belong to juliet 
    possible_nrs_for_juliet = []

    # I need to add a number everywhere and check if the number is in wa_nrs
    for i in range(7):
        for k in range(0, 10):
            if (n[:i+2] + str(k) + n[i+2:]) in wa_nrs:
                if (n[:i+2] + str(k) + n[i+2:]) not in possible_nrs_for_juliet:
                    possible_nrs_for_juliet.append(n[:i+2] + str(k) + n[i+2:])
    for k in range(0, 10):
        if (n + str(k)) in wa_nrs:
            if (n + str(k)) not in possible_nrs_for_juliet:
                possible_nrs_for_juliet.append((n + str(k)))

    return possible_nrs_for_juliet
    # Don't forget to return your result

# For this particular number, the function should find the
# last element in wa_nrs
print(get_possible_nrs("076432165"))
