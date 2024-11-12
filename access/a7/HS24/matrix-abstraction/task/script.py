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