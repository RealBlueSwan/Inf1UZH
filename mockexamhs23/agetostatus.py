def classify(name, age, child, adult, senior):
    
    if age in range(0, child):
        return f'{name} is an infant'
    elif age in range(child, adult):
        return f'{name} is a child'
    elif age in range(adult, senior):
        return f'{name} is an adult'
    else:
        return f'{name} is a senior'

print(classify("Bobby", 4,  5, 18, 65))
print(classify("Bobby", 5,  5, 18, 65))
print(classify("Bobby", 25, 5, 18, 65))