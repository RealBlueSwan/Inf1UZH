#!/usr/bin/env python3

class Matrix:
    def __init__(self, data):
        # Assertions to validate the input data
        assert isinstance(data, list) and all(isinstance(row, list) for row in data), "Data must be a list of lists"
        assert all(isinstance(val, (int, float)) for row in data for val in row), "All values must be integers or floats"
        assert len(data) > 0 and all(len(row) == len(data[0]) for row in data), "All rows must have the same length and there must be at least one non-empty row"
        assert data != [[]], "Matrix cannot be instantiated with an empty row"
        self._data = data

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self._data))
    
    def __eq__(self, other):
        return (self._data == other._data)

    def __add__(self, other):
        assert len(self._data) == len(other._data) and len(self._data[0]) == len(other._data[0]), "Matrices must have the same dimensions"
        result = [
            [self._data[i][j] + other._data[i][j] for j in range(len(self._data[0]))] for i in range(len(self._data))
        ]
        return Matrix(result)

    def __mul__(self, other):   # the first element in the new matrix is supposed to be the sum of the first row and the first column 
        result = [  
            [(sum(self._data[i][k] * other._data[k][j] for k in range(len(self._data[0])))) for j in range(len(self._data[0]))] for i in range(len(self._data))
        ]
        return Matrix(result)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self._data])

    def __repr__(self):
        return f"Matrix({self._data})"

m = Matrix([[5,5],[5,5]])
t = Matrix([[5,5],[5,5]])
# equal?
print(m == t)
# hashes equal?
print((hash(m) == hash(t)))
# can be used as dictionary key?
d = {m: "1", t: "2"}
d.update({m: "3"})
# add and multiply
print(m + t)
print(m * t)

try:
    invalid_matrix = Matrix([[]])
except AssertionError as e:
    print(f"AssertionError: {e}")

try:
    m1 = Matrix([[1, 2]])
    m2 = Matrix([[1]])
    print(m1 + m2)
except AssertionError as e:
    print(f"AssertionError: {e}")

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
 * Implement `__add__` so that two instances of class `Matrix` can be added via the `+` operator.
 * Implement `__mul__` so that two instances of class `Matrix` can be multiplied via the `*` operator.
 * Implement `__eq__` so that two instances of class `Matrix` can be compared via the `==` operator.
 * Implement `__hash__` so that instances of class `Matrix` can be used as dictionary keys.


**Note:** In case you do not know how to add/multiply matrices, check this [Link](https://en.wikipedia.org/wiki/Matrix_(mathematics)#Matrix_multiplication)

**Note:** To read more about `__add__` and `__mul__`, checkout the [appropriate documentation](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)

**Note:** We encourage you to experiment with your data structure to understand the effect that providing the various methods has on the way in which you can use your data structure.

**Note:** All state must be contained within the class. Do not store information in global variables or in class variables. It has to be possible to use multiple instances of the classes in parallel without suffering from side effects.

**Note:** The provided files define the signatures of various classes and functions. Do not change these signatures or the automated grading will fail.

**Note:** We strongly encourage you to add more tests to the public test suite.

"""