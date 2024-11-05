

def both(f, g, it):
    return (f(it), g(it))


print( both(str.lower, str.upper, "HeLlO") )    # ('hello', 'HELLO')
print( both(int, float, "1") )                  # (1, 1.0)
