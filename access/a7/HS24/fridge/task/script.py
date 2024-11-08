#!/usr/bin/env python3

class Fridge:
    # Datastructure:
    def __init__(self):
        self.itemlist = []

    def __len__(self):
        return len(self.itemlist)

    def __iter__(self):
        self.itemlist.sort()
        return iter(self.itemlist)
    
    # Transformers: 
    def store(self, data):
        self.itemlist.append(data)

    def take(self, data):
        item = self.find(data)
        if item is not None and item == data:
            self.itemlist.remove(item)
            return item
        elif item is None:
            raise Warning(f"{data[1]} couldn't be found")

    def find(self, data):
        for item in self.itemlist:
            if item == data:
                return item
        return None 
        
    def take_before(self, date):
        items_to_remove = [item for item in self.itemlist if item[0] < date]
        for item in items_to_remove:
            self.itemlist.remove(item)
        return items_to_remove


f = Fridge()
f.store((191127, "Butter"))
f.store((191117, "Milk"))

f.take((191127, "Butter"))  # ok
f.take((191207, "Bread"))  # fails
print(f.take_before(191119))