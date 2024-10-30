#!/usr/bin/env python3

class MagicDrawingBoard:
    def __init__(self, x, y):       # Initiate the variables and check if they are not <= 0
        if x <= 0 or y <= 0:
            raise ValueError("The board can not be smaller or equal 0")
        self.x = x
        self.y = y
        self.reset()                # Create new bord

    def reset(self):                # Create new bord
        self.bord = self.x * self.y * [0]

    def _idx(self, xy):             # find out where in the bord the coords are and return an int
        x, y = xy
        return y*self.x + x

    def _assert_coords(self, xy, is_end = False):
        x, y = xy
        
        if x<0 or y<0 or y>self.y or x>self.x:              # check smaller than 0 or outside of bord
            raise ValueError("Coordinates out of bound.")
        
        if not is_end:                                      # this is in case the coord is outside the bord
            if x==self.x or y==self.y:
                raise ValueError("only end_point coordinate can be outside of bord.")

    def pixel(self, xy):            # draw at one coordinate
        self._assert_coords(xy)     # Check if the pixel is valid
        idx = self._idx(xy)         # Which number coresponds to those cooridnates
        self.bord[idx] = 1          # Changes the entry in the list

    def rect(self, start, end):     # Creates a rect at coordinate
        self._assert_coords(start)      # assert Cords start
        self._assert_coords(end, True)  # assert cords end, True

        # Check if the width and height are bigger than 0
        width = end[0] - start[0]
        height = end[1] - start[1]
        if width < 1 or height < 1:
            raise ValueError("Height or Width must be greater than 0.")
        
        # BUG: there is something printing stuff wrong. 
        idx_start = self._idx(start)                                        # defines where the rectangle starts
        for delta_x in range(width):                                        # at this x in the y plain
            for delta_y in range (height):                                  # at this current y plain
                cur = idx_start + delta_x + delta_y * self.x                # Calculates the corresponding 
                self.bord[cur] = 1                                          # This changes the 0 to 1 at cur
                                          
    def img(self):                  # Returns the img
        # define width and print line for line of bord
        bord = ''
        for idx, v in enumerate(self.bord):
            if idx % self.x == 0 and idx > 0: 
                bord += '\n'
            bord += '1' if v else '0'
        print(bord)
        return bord

        
        

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    db = MagicDrawingBoard(6,4) # instantiation of a specific size
    db.pixel((1,1)) # draw at one coordinate
    db.rect((2,2), (5,4)) # draw a rectangle
    img = db.img() # return the drawn image
    db.reset() # reset the field again
