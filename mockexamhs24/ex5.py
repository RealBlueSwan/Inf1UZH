def caser(s):
    if len(s) <= 5:
        return s.lower()
    else:
        return s.upper()


print( caser("Hello") )             # hello
print( caser("Bananas") )           # BANANAS
print( caser("AbC") )               # abc
print( caser("i don't know!") )     # I DON'T KNOW!

