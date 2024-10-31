def strings_containing(strings, word):
    for n in strings:
        n = n.lower()
        if word not in n:
            strings.remove(n)

    return strings


print( strings_containing(["Hello", "there", "friend"], "he" ) )
print( strings_containing(["abc", "cde", "DEF"], "de" ) )


#['Hello', 'there']
#['cde', 'DEF']