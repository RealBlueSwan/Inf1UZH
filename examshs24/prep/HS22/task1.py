def to_list(thing, fnc = lambda x: [x]):

    try:
        return list(thing)
    except:
        return fnc(thing)


print( to_list([1,2,3]) )
print( to_list((1,2,3)) )
print( to_list(1.5) )
print( to_list(True) )
print( to_list(True, lambda x: [int(x)]) )

