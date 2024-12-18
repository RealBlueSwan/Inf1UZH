"""
Implement a class Order, which takes two parameters in its constructor:

items, a list of strings
cost, a number
These two values should be stored as instance attributes.

The Order class should implement the equality operator as follows. Two instances of Order are equal if and only if the list of items contains the same strings and if the cost is the same. Mind that the same item may appear multiple times in an order. Do not forget to correctly handle cases where the value being compared to is not an instance of Order.

You may assume that Order will only be constructed with parameters that match the description.
"""

class Order:
    def __init__(self, items, cost):
        self.items = items
        self.cost = cost
    
    def __eq__(self, other):
        if not isinstance(other, Order):
            return NotImplemented
        
        # Two instances of Order are equal if and only if the list of items contains the same strings and if the cost is the same. 
        # Mind that the same item may appear multiple times in an order. 
        # Do not forget to correctly handle cases where the value being compared to is not an instance of Order.
        return self.cost == other.cost and sorted(self.items) == sorted(other.items)


print( Order(["Beer", "Wine", "Beer"], 14.50) == Order(["Wine", "Beer", "Beer"], 14.50) )
print( Order(["Beer", "Wine", "Beer"], 14.50) != Order(["Wine", "Beer"], 14.50) )
print( Order(["Beer", "Pretzels"], 14.50) == "Healthy meal" )


"""
True
True
False
"""