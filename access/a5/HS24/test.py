list1 = []
counter = 1

def counter_test(c):
    c += 3

def global_counter_test():
    global counter
    counter += 2 

def list_test(l):
    l.append(1)



# Counter in the function does not change Global var
print(counter)

counter_test(counter)
print(counter)


# A gloabl counter...
print(counter)

global_counter_test()
print(counter)


# Append acts globally -> "because it points to a list and list is like stack?"
print(list1)

list_test(list1)
print(list1)