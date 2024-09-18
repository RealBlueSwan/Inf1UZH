#!/usr/bin/env python3

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return self.name

class Order:
    def __init__(self, items):
        self.items = items

    def bill_amount(self):
        return sum(item.price for item in self.items)

    def __repr__(self):
        return f"Order Items: {self.items}, Bill Amount: {self.bill_amount()}"

class Restaurant:

    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
        self.orders = []

    def order(self, ordered_items):
        available = [i for i in ordered_items if i in self.menu]
        if len(available) > 0:
            self.orders.append(Order(available))

    def get_revenue(self):
        return sum([o.bill_amount() for o in self.orders])

