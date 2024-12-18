"""
Implement a class Market that keeps track of how much vendors are paying for having a stall at a market during a day.

A market rents out stalls on an hourly basis. The market and the vendors agree on an hourly fee when the vendor joins the market. The vendor then pays the fee for each hour they stay on the market until they leave.

The Market class should support adding new vendors with a given hourly fee. It should have a method progress_hour that runs the clock one hour forward (the clock starts at zero). It should keep track internally of how many vendors there are and what fees they are paying. A method stats should return a dictionary that lists:

the number of vendors
the current hour
the hourly profit that can be made given the currently present vendors and
the total profit made so far
Important: The examples contain essential information, such as how the methods should be called and used and what the stats dictionary should look like. Make sure your implementation works with the provided examples.

Use the following template:
"""
class Market:
    def __init__(self):
        self.vendors = []
        self.total_profit = 0
        self.hour = 0

    def stats(self):
        return f"'number of vendors': {len(self.vendors)}, 'hour': {self.hour}, 'hourly profit': {sum(self.vendors)}, 'total profit': {self.total_profit}"

    def add_vendor(self, value):
        self.vendors.append(value)

    def remove_vendor(self, value):
        try:
            self.vendors.remove(value)
        except:
            raise Warning("No vendor with that fee exists")

    def progress_hour(self):
        self.hour += 1
        self.total_profit += sum(self.vendors)


m = Market()
print(m.stats())
m.add_vendor(30)
m.add_vendor(5)
m.add_vendor(5)
print(m.stats())
m.progress_hour()
m.progress_hour()
m.progress_hour()
print(m.stats())
try:
    m.remove_vendor(11)
except:
    print("No vendor with that fee exists")
m.remove_vendor(5)
print(m.stats())
m.progress_hour()
print(m.stats())


"""
{'number of vendors': 0, 'hour': 0, 'hourly profit': 0, 'total profit': 0}
{'number of vendors': 3, 'hour': 0, 'hourly profit': 40, 'total profit': 0}
{'number of vendors': 3, 'hour': 3, 'hourly profit': 40, 'total profit': 120}
No vendor with that fee exists
{'number of vendors': 2, 'hour': 3, 'hourly profit': 35, 'total profit': 120}
{'number of vendors': 2, 'hour': 4, 'hourly profit': 35, 'total profit': 155}
Paste your solution into the following field. Utilize the template above and make absolutely sure to avoid syntax errors! Submit everything that is necessary to import your solution - not more, not less!
"""
