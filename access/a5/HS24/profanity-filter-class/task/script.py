#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.
class ProfanityFilter:

    def __init__(self, keywords, template):
        self.keywords = reversed(sorted([kw.lower() for kw in keywords]))
        self.template = template

    def filter(self, msg):
        # Unify
        msg_lower = msg.lower()
        for word in self.keywords:                              # Word in keywords and start replacing if match
            while word in msg_lower:                            # repeat as long as in msg
                idx = msg_lower.find(word)                      # Where is the word in the sentence?
                msg = self.replace(msg, idx, word)              # Replace the word in msg with filterword
                msg_lower = self.replace(msg_lower, idx, word)  # Replace the word in msg_lower with filterword
        return msg

    def replace(self, s, idx, word):                            # Brain for returning a clean word
        clean_word = self.escape(word)                          # Creates a clean wordsniplett
        return s[:idx] + clean_word + s[idx+len(clean_word):]   # Returns the clean word 

    def escape(self, word):                                     # Filtercreator function for parent
        res = ''                                                # Temp res for return
        for idx, _ in enumerate(word):                          # Creates Index for every letter in word
            t_idx = idx % len(self.template)                    # Creating temp_idx which char in template to add
            res += self.template[t_idx]                         # Adds letter to res
        return res                                              # Returns res/clean_word


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghshoti mastard jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno


"""
f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
offensive_msg = "He's a complete mastard!"
clean_msg = f.filter(offensive_msg)
print(clean_msg)                       # He's a complete ?#$?#$?!
"""