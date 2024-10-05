#!/usr/bin/python3

# Implement the following three functions according to the specification.

def add_stock(warehouse, product):
    # Check if the product is in warehouse
    if product in warehouse:
        # Add 1 to stock
        warehouse[product] += 1
    else:
        # Add product to warehouse
        warehouse[product] = 1
    
    return warehouse
    

def remove_stock(warehouse, product):
    # Check is product in warehouse
    if product not in warehouse:
        print(f"{product} not in stock")
        return warehouse
    
    # Check if only one product in warehouse in order to del
    if warehouse[product] == 1:
        del warehouse[product]
    else:
        # Remove 1
        warehouse[product] -= 1
    
    return warehouse

def get_stock(warehouse, product):
    if product not in warehouse:
        return 0
    else:
        return warehouse[product]

# The following code is just here as an example for you to try your
# implementation. Uncomment it and run it if you want. Feel free to modify it.
# However, make sure it doesn't break your solution when submitting.

#warehouse = { "A": 10, "B": 15, "C": 1, "D": 2 }
#add_stock(warehouse, "A")    # stock for A should now be 11
#print(warehouse)
#remove_stock(warehouse, "D") # stock for D should now be 1
#remove_stock(warehouse, "C") # The key/value pair for key "C" should be removed
#remove_stock(warehouse, "X") # should print: X not in stock
#get_stock(warehouse, "B")    # should return 15
#get_stock(warehouse, "C")    # should return 0
#print(warehouse)             # to see if it worked

