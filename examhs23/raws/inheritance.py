from abc import ABC, abstractmethod

class Restaurant:
    def __init__(self, employee):
        self.employee = employee

class Staff:
    pass
class Server:
    pass
class Dishwasher:
    pass
class Cook:
    def __init__(self, resturant, hours):
        self.hours = hours
        self.hours = []

    def work(self, hours):
        return hours.append(hours)



restaurant = Restaurant("Mc Ronalds")
cook = Cook(restaurant, 3200)
cook.work(10)
cook.work(50)
print(cook.number)
print(cook.shifts)
print(type(cook.shifts))
print(cook.salary())
print(cook)
server = Server(restaurant, 100, 9.50)
server.work(10)
server.work(50)
print(server.number)
print(server.shifts)
print(server.salary()) # (100 + 60*9.50)
washer = Dishwasher(restaurant, 100, 9.50)
washer.work(10)
washer.work(50)
print(washer.number)
print(washer.shifts)
print(washer.salary()) # (100 + 60*9.50) * 0.9