
class Rider:
    def __init__(self, fname, lname, ticket_class):
        self.fname = fname
        self.lname = lname
        self.ticket_class = ticket_class
        
    def __repr__(self):
        class_str = "general"
        if self.ticket_class == "D":
            class_str = "day"
        if self.ticket_class == "M":
            class_str = "monthly"
        return f"{self.fname} {self.lname}, {class_str} ticket"
        

class Train:
    def __init__(self, trainnumber, trainname):
        self.trainnumber = trainnumber
        self.trainname = trainname
        self.riders = []

    @staticmethod
    def parse_reservations(reservations):
        return [Rider(f, l, t) for f, l, t in [passenger.split(',') for passenger in reservations.split(';')]]

    def board(self, p):
        self.riders.extend(p)

    def get_riders(self, ticket_class = None):
        if ticket_class == None:
            return self.riders
        return [p for p in self.riders if p.ticket_class == ticket_class]



riders = Train.parse_reservations(("Montgomery,Rich,GA;Tim,Merchant,GA;Sally,Sale,D;Peter,Poor,M"))
a = Train("IC17", "Columbus")
a.board(riders)
print(a.get_riders())
p = a.get_riders("GA")
print(type(p[1]))
print(p[1])
# The code above should produce the following output:

# [Montgomery Rich, general ticket, Tim Merchant, general ticket, Sally Sale, day ticket, Peter Poor, monthly ticket]
# <class '__main__.Rider'>
# Tim Merchant, general ticket
