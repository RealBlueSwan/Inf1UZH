#!/usr/bin/env python3
from collections import Counter

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def analyze(posts):
    hashtags = []
    temphash = []
    words = [word for post in posts for word in post.split(" ")]

    for word in words:
        word = word.replace('.', '')
        #print(word)
        if word[0] == '#' and len(word) > 1:
            #print(ord(word[1]))
            word = word.replace('#', '')
            #check if first letter is only char
            if ord(word[1]) in range(65, 91) or ord(word[1]) in range(97, 123):
                #check if there are only char and numb
                #48, 58
                #print(word)
                temphash.append(word)
                #test if the word is not in hashtags
            
    hashtags = Counter(temphash)

    return hashtags
    '''
    for post in posts:
        #split the post into words
        for word in post.split(" "):
            print(word)

            #append every word starting with a hashtag to a list and enumerate. 
        
        
        #find the hashtag
        print(post.find('#'))
    '''
        
# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = [
    "hi #weekend",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich",
    "#zurich <3",
    "#"
    ]
print(analyze(posts))
