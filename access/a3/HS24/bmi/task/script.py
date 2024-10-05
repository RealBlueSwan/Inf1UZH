#!/usr/bin/env python3

# Height in M
height = 10
# Weight in KG
weight = 10

# Determine the BMI. Change the function
# below to calculate the BMI return which category the result is in.
# Your implementation should work with any specific value.
# You must use the variables defined above.

def get_bmi_category(height, weight):
    weight_float = float(weight)
    height_float = float(height)
    
    # Calculate BMI
    bmi = weight_float / height_float**2
    
    # Determine the category
    if bmi <= 0 or weight_float <= 0 or height_float <= 0:
        return "N/A"
    elif bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Pre-obesity"
    elif 30 <= bmi < 35:
        category = "Obesity class I"
    elif 35 <= bmi < 40:
        category = "Obesity class II"
    elif bmi >= 40:
        category = "Obesity class III"
    else:
        return "Something went wrong"
    
    return f"BMI: {bmi:.2f}, Category: {category}"

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(get_bmi_category(height, weight))
