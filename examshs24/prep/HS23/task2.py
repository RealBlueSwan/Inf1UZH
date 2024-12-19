"""
Implement a class Data which takes a list of objects as the only constructor argument and refers to it using a public attribute data.

Data should provide a method compute which takes two functions as arguments. compute should call the given functions with the Data object's data as the argument and return the two resulting values in a tuple.

The Data class should work with arbitrary data types, as long as any functions passed are compatible with whatever data is stored.

Use the following template:
"""

class Data:
    def __init__(self, data):
        self.data = data

    def compute(self, salt, pepper):
        return (salt(self.data), pepper(self.data))


# The following example illustrates how the solution may be used:

objects = [1.7, 2.3, 3, 4]
d = Data(objects)
print( d.data is objects )
print( d.compute(sum, min) )
print( d.compute(min, max) )

"""
The code above should produce the following output:

True
(11.0, 1.7)
(1.7, 4)
"""