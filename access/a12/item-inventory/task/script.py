#!/usr/bin/env python3

class Inventory:
    def __init__(self, player_name="DEFAULT", balance=0, max_weight=0):
        self.__player_name = player_name
        self.__balance = balance
        self.__weight_cap = max_weight
        self.__content = []
    
    def collect(self, item):
        # check if item is a "proper item"
        self.__proper_item(item)
        # check if the current weight plus the item weight would exceed the max weight
        if (self.get_inv_weight() + item[2]) > self.__weight_cap:
            raise Warning("Inventory is too heavy.")
        self.__content.append(item)

    def get_inv_weight(self):
        return sum([item[2] for item in self.__iter__()])

    def get_balance(self):
        return self.__balance

    def get_inv_value(self):
        return sum([item[1] for item in self.__iter__()])

    def drop(self, item):
        self.__proper_item(item)
        #test if the item is in the __content 
        if item in self.__content:
            self.__content.remove(item)
            return item
        
        raise Warning("no such item in inventory")

    def sell(self, item):
        self.__proper_item(item)
        #test if the item is in the __content 
        if item in self.__content:
            self.__balance += item[1]
            self.__content.remove(item)
            return item
        raise Warning("no such item in inventory")

    def buy(self, item):
        # check if item is a "proper item"
        self.__proper_item(item)
        # check if the current weight plus the item weight would exceed the max weight
        if (self.get_inv_weight() + item[2]) > self.__weight_cap:
            raise Warning("Inventory is too heavy.")
        # check if there is enough balance
        if (self.__balance - item[1]) < 0:
            raise Warning("youre broke ma dude")
        self.__balance -= item[1]
        self.__content.append(item)
        return item
    
    def get_player_name(self):
        return self.__player_name

    #implement this function to check if a given object fits the described type for an item (3-tuple of string, int, int)
    #raise a Warning if it doesn't
    def __proper_item(self, item):
        if item != (str, int, int):
            raise Warning("not propper item")
        

    def __iter__(self):
        return iter(sorted(self.__content, key=lambda item: item[1], reverse=True))

    def __len__(self):
        return len(self.__content)

