class StringDict:
    pass


d1 = StringDict()
print(d1)
d1[1] = 100
d1["abc"] = print
print(d1)
print(isinstance(d1[1], str))
print(1 in d1)
print(100 in d1)
print(len(d1))
d2 = StringDict({"abc": print, 1: "100"})
d3 = StringDict({"abc": max})
print(d1 == d2)
print(d1 == d3)