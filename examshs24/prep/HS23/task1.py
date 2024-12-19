"""
Implement a class Data which takes a list of objects as the only constructor argument and refers to it using a public attribute data.

Data should provide a method compute which takes a function as the only parameter. compute should call the given function on each element in data and return the resulting values in a list (in the same order as the elements in data).

The Data class should work with arbitrary data types, as long as any functions passed are compatible with whatever data is stored.

Use the following template:
"""

class Data:
    def __init__(self, data):
        self.data = data
    
    def compute(self, function):
        return [function(f) for f in self.data]


# The following example illustrates how the solution may be used:
objects = [1.7, 2.3, 3, 4]
d = Data(objects)
print( d.data is objects )
print( d.compute(str) )
import math
print( d.compute(math.floor) )
"""
The code above should produce the following output:

True
['1.7', '2.3', '3', '4']
[1, 2, 3, 4]
"""