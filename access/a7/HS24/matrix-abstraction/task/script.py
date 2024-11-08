#!/usr/bin/env python3

class Matrix:
    
    def __init__(self, matrix):
        
        if len(matrix) == 2 and len(matrix[0] == 2) and len(matrix[1] == 2):
            self.matrix = matrix
        else:
            raise AssertionError("Matrix does not satisfy the needs")
        
        for row in matrix:
            for element in row:
                if type(element) != int and type(element) != float:
                    raise AssertionError("one element in matrix is not int or float")
                
        if len(matrix[0]) != len(matrix[1]):
            raise AssertionError("The provided matrix contains row of different length")


    def __eq__(self, other):
        pass

    def __hash__(self):
        return hash(self.matrix)

    def __add__(self, other):
        for y in self.matrix:
            for x in y:
                self.matrix[y][x] = self.matrix[y][x] + other.matrix[y][x]
        
        return self.matrix
    
    def __mul__(self, other):
        pass


    """
    * Each nested list corresponds to one row in the matrix
    * The indices within a nested list correspond to the columns.
    * If the constructor input satisfies the following properties it should be stored as a **private** instance variable:
    1. It contains exactly 2 dimensions.
    2. All values contained in nested lists are integers and/or floats.
    2. All nested lists have the same length.
    3. There has to be at least one non-empty row (in other words: `[[]]` would be invalid).
    * If the above conditions are not satisfied, an `AssertionError` should be thrown
    (you may use the `assert x == y, "error message in case of assertion failure"` syntax).
    """
    pass
    # Also, implement the special methods __eq__, __hash__, __add__, and __mul__
    # as per the task description.

    # def __eq__(self, other):
    #   etc ...

# Make sure to work on task/tests.py as well to test your implementation!


"""
m = Matrix([[5,5],[5,5]])
t = Matrix([[5,5],[5,5]])
# equal?
# hashes equal?
self.assertTrue(hash(m) == hash(t))
# can be used as dictionary key?
d = {m: "1", t: "2"}
d.update({m: "3"})
# add and multiply
m + t
m * t
"""