"""
When attempting to create a Wrapper or Box with an unsupported number of Cookies, a Warning should be raised.
Make sure to minimize code duplication.
The provided examples contain valuable information on how the solution should work. Your solution must be compatible with the provided examples.
Do not include any example calls in your submission. Submit only top-level class definitions and any imports you might need.
Some points will be given for each feature that works correctly, some points will be given for optimally designing the implementation. Recommendation: prioritize implementing a solution that works correctly with the provided examples. Optimize the design afterwards.
Use the following template:
"""

from abc import ABC, abstractmethod

class Cookie:                   # Each cookie produced is given a name and a price. It should be possible to find out the name and price of a cookie.
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price

# The factory ships cookies in different kinds of containers, namely wrappers and boxes, maybe more in future -> ABS
class Container(ABC):
    def __init__(self, content):
        self.__content = content

    # total price rounded to two decimal points
    def get_price(self):
        return round(sum([w.get_price() for w in self.__content]), 2) 

    def get_contents(self):
        return self.__content

    @abstractmethod
    def get_number_of_cookies(self):
        pass

class Wrapper(Container):               # A wrapper is used to hold between 3 and 5 cookies.
    def __init__(self, cookies):
        super().__init__(cookies)
        if len(cookies) > 5 or len(cookies) < 3:
            raise Warning
        
    def get_number_of_cookies(self):
        return len(self.get_contents())

class Box(Container):                   # Boxes are used to ship multiple wrappers.
    # For quality control, each box shall have a unique retrievable ID, starting at 1 for the first box and incrementing by 1 for each additional box produced.
    seq = 1
    def __init__(self, wrappers):
        super().__init__(wrappers)
        if self.get_number_of_cookies() > 200:  # A box can contain at most 200 cookies, no matter how many wrappers have been used to hold them.
            raise Warning
        self.__id = Box.seq
        Box.seq += 1
    
    def get_id(self):
        return self.__id
    
    def get_number_of_cookies(self):
        return sum([w.get_number_of_cookies() for w in self.get_contents()])

def make_cookies(n):
    return [Cookie("Chocolate", 0.50) if x % 2 == 0 else Cookie("Vanilla", 0.60) for x in range(n)]

cookies = make_cookies(4)
print(cookies[0].get_name())
print(cookies[0].get_price())

w1 = Wrapper(cookies)
print([c.get_name() for c in w1.get_contents()])

w2 = Wrapper(make_cookies(4))
b = Box([w1, w2])
print(f"\nCookies in box: {b.get_number_of_cookies()}")
print(f"  Price of box: {b.get_price()}")
print(f"     ID of box: {b.get_id()}\n")

more_wrappers = [Wrapper(make_cookies(4)) for x in range(52)] # 208 cookies
try:
    overfull = Box(more_wrappers)
except Warning:
    print("Too many cookies for one box\n")


"""
Chocolate
0.5
['Chocolate', 'Vanilla', 'Chocolate', 'Vanilla']

Cookies in box: 8
  Price of box: 4.4
     ID of box: 1

Too many cookies for one box
"""