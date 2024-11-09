# Task: Publication Data Structure

Implement a data structure called `Publication` to represent scientific articles. Each `Publication` will have a list of authors, a title, and a year of publication. Your implementation should support comparison operators, string representation, and immutability.

## Current Implementation Status

### Class Definition
- The `Publication` class has been defined with the following attributes:
  - `authors`: A list of authors.
  - `title`: The title of the publication.
  - `year`: The year of publication.

### Methods Implemented
- `__init__`: Initializes the `Publication` object with authors, title, and year.
- `__eq__`: Compares two `Publication` objects for equality.
- `__str__` and `__repr__`: Provides string representation of the `Publication` object.

### Comparison Operators
- `__le__`: Partially implemented to compare `Publication` objects. Needs completion and implementation of other comparison operators (`<`, `<=`, `>`, `>=`).

### Immutability
- The attributes are currently public and mutable. Need to make them private and provide getter methods to ensure immutability.

### Example Usage
