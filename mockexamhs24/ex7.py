from urllib.parse import quote


def encode(s):
    return quote(s)
    


print( encode("/El Niño/") )        # /El%20Ni%C3%B1o/
print( encode("Hello, world!") )    # Hello%2C%20world%21



