#!/usr/bin/env python3

# Calculate the tax.
# Change the functions below to calculate the right tax and return the amount.

# Standard tax rate is 8.1%
def standard_tax(amount):
    return round_tax(amount * 0.081)

# Reduced tax rate is 2.5%
def reduced_tax(amount):
    return round_tax(amount * 0.025)

# Accommodation tax rate is 3.7%
def accommodation_tax(amount):
    return round_tax(amount * 0.037)

# Helper function to round the tax to the nearest 0.05 increment.
def round_tax(tax):
    return round(round(float(tax) / 0.05) * 0.05, 2)

# Main function
def calculate_tax(amount, tax_type):
    if amount < 0:
        return 0.0
    return tax_type(amount)

# The following lines call the function and prints the return
# value to the Console. This way you can check what it does.
print(calculate_tax(101, standard_tax))  # Expected: 8.15
print(calculate_tax(101, reduced_tax))  # Expected: 2.55
print(calculate_tax(101, accommodation_tax))  # Expected: 3.75
print(calculate_tax(-1, standard_tax))  # Expected: 0.0
print(calculate_tax(-1, reduced_tax))  # Expected: 0.0
print(calculate_tax(-1, accommodation_tax))  # Expected: 0.0