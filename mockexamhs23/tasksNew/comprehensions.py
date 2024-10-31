# Implement a function strings_containing which takes two parameters: a list of strings strings and a string word. 
# The function should return a list of strings from strings containing only those strings that contain word (in the original order), ignoring character casing.

# You may assume that your function will only be called with parameters that match the given description.

# Important: The function must start with return and it must return a comprehension outright. You are not allowed to build data structures using for loops or declare temporary variables.

# Use the following template:

def strings_containing(strings, word):
    return [string for string in strings if word.lower() in string.lower()]
# The following example illustrates how the solution may be used:

print( strings_containing(["Hello", "there", "friend"], "he" ) )        # ['Hello', 'there']
print( strings_containing(["abc", "cde", "DEF"], "de" ) )               # ['cde', 'DEF']
