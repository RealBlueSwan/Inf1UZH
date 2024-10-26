#!/usr/bin/env python3

class MagicDrawingBoard:
    def __init__(self, x, y):
        self.bord = [ [False] * x ] * y     # I need to figure out how to implement this and make it a string and not a list... wait... does not need to be a string, can be true and false and then I just parce over it at img()!


    """
     "000000\n
    010000\n
    001110\n
    001110"
    """

    def pixel(self, cord):          # draw at one coordinate
        
        pass

    def rect(self, start, end):     # Creates a rect at coordinate
        pass

    def reset(self):                # Resets the board
        pass

    def img(self):                  # Returns the img
        #{print(row) for row in self.bord}
        temp_all = ''
        for row in self.bord:
            temp_row = ''
            for _ in self.bord:
                pass                    # Here is all the fun :DDDDDD
            temp_all = temp_row + '\n'

        return temp_all
        
        

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    db = MagicDrawingBoard(6,4) # instantiation of a specific size
    db.pixel((1,1)) # draw at one coordinate
    db.rect((2,2), (5,4)) # draw a rectangle
    img = db.img() # return the drawn image
    db.reset() # reset the field again
