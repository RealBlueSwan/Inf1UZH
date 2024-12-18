"""
Read the example calls and provided output below. Then implement the necessary class(es) such that they will produce the same output given the example calls.

The following example illustrates how the solution may be used:
"""

class Passenger:
    def __init__(self, fname, lname, ticket_class):
        self.fname = fname
        self.lname = lname
        self.ticket_class = ticket_class
    
    def __repr__(self):
        # ifs and elses.... needs to match output down below! 
        class_str = "1st"
        if self.ticket_class == 2:
            class_str = "business"
        if self.ticket_class == 3:
            class_str = "economy"

        return f"{self.fname} {self.lname}, {class_str} class"

class Airplane:
    def __init__(self, number, serialnumber):
        self.number = number
        self.serialnumber = serialnumber
        self.classes = [[], [], []]

    @staticmethod
    def parse_manifest(manifest):
        return [Passenger(f, l, int(t)) for f, l, t in [m.split(',') for m in manifest.split(";")]]
    
    def board(self, passengers):
        for p in passengers:
            self.classes[p.ticket_class-1].append(p)

    def get_passengers(self, ticket_class = None):
        if ticket_class == None:
            res = []
            for c in self.classes:
                res.extend(c)
            return res
        return self.classes[ticket_class-1]


passengers = Airplane.parse_manifest(("Montgomery,Rich,1;Tim,Merchant,2;Sally,Sale,2;Peter,Poor,3"))
a = Airplane("A388", "G-XLEK")
a.board(passengers)
print(a.get_passengers())
p = a.get_passengers(2)
print(type(p[1]))
print(p[1])


# The code above should produce the following output:
"""
[Montgomery Rich, 1st class, Tim Merchant, business class, Sally Sale, business class, Peter Poor, economy class]
<class '__main__.Passenger'>
Sally Sale, business class
"""
