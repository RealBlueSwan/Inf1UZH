"""
implement two functions encode and decode that work correctly with the following example calls. First, try to understand what these functions do. Note that decode implements the reverse operations from encode and that each function returns three values, which represent the intermediate and final states reached within the respective functions. The parameters of each function are the input string to be encoded and the two modification parameters that influence how the intermediate transformations are performed. Your solution should also work if these modification parameters take on any other kind of value of the same type as given in the examples, although the second string passed to encode or decode will never be empty.

Use the following template:

# Your implementation of the necessary class(es)
"""


def encode(string, pattern, asciikey):
    stringlist = []
    for idx in range(len(string)):
        stringlist.append(string[idx])
        stringlist.append(pattern[idx%len(pattern)])
    
    asciilist = [ord(char)+ asciikey for char in stringlist]
    encstring = ''.join([chr(char) for char in asciilist])
    return stringlist, asciilist, encstring


def decode(string, pattern, asciikey):
    
    enc_string = [ord(char) for char in string]

    deasciishift = [chr(char-asciikey) for char in enc_string]

    decodedstring = ''.join([deasciishift[idx] for idx in range(len(deasciishift)) if idx%2 == 0])

    return enc_string, deasciishift, decodedstring



# The following example illustrates how the solution may be used:

print(encode("hello", "xyz", -2) == (['h', 'x', 'e', 'y', 'l', 'z', 'l', 'x', 'o', 'y'], [102, 118, 99, 119, 106, 120, 106, 118, 109, 119], 'fvcwjxjvmw'))
print(decode("fvcwjxjvmw", "xyz", -2) == ([102, 118, 99, 119, 106, 120, 106, 118, 109, 119], ['h', 'x', 'e', 'y', 'l', 'z', 'l', 'x', 'o', 'y'], 'hello'))
# The code above should produce the following output:

"""
True
True
"""