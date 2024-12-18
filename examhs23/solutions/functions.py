objects = [1.7, 2.3, 3, 4]

class Data:
    def __init__(self, objects):
        self.objects = objects
        

    def compute(self, one, two):
        returnval = []
        if one == 'sum':
            returnval.append(sum(objects))
        if one == 'min':
            returnval.append(min(objects))
        if one == 'max':
            returnval.append(max(objects))
        if two == 'min':
            returnval.append(min(objects))
        if two == 'max':
            returnval.append(max(objects))
        if two == 'sum':
            returnval.append(sum(objects))
        return returnval
        

d = Data(objects)

#print( d.data is objects )
print( d.compute(sum, min) )
print( d.compute(min, max) )