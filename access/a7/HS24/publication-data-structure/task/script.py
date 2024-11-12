#!/usr/bin/env python3

class Publication:

    def __init__(self, authors, title, year):
        self.__authors = list(authors)
        self.__title = title
        self.__year = year

    def __eq__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return (self.__authors == other.__authors and self.__title == other.__title and self.__year == other.__year)

    def __hash__(self):
        return hash((tuple(self.__authors), self.__title, self.__year))

    def __str__(self):
        authors_str = ', '.join(f'"{author}"' for author in self.__authors)
        return f'Publication([{authors_str}], "{self.__title}", {self.__year})'

    def __repr__(self):
        authors_str = ', '.join(f'"{author}"' for author in self.__authors)
        return f'Publication([{authors_str}], "{self.__title}", {self.__year})'

    def __le__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        if self.__authors != other.__authors:
            return self.__authors < other.__authors
        if self.__title != other.__title:
            return self.__title < other.__title
        return self.__year <= other.__year

    def __lt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        if self.__authors != other.__authors:
            return self.__authors < other.__authors
        if self.__title != other.__title:
            return self.__title < other.__title
        return self.__year < other.__year

    def __ge__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return not self < other

    def __gt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return not self <= other

    def get_authors(self):
        return list(self.__authors)

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

if __name__ == '__main__':
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    print(p)
    print(str(p) == s)

    p1 = Publication(["A"], "B", 1234)
    p2 = Publication(["A"], "B", 1234)
    p3 = Publication(["B"], "C", 2345)
    print(p1 == p2)  # True
    print(p2 == p3)  # False
    
    sales = {
        p1: 273,
        p2: 398,
    }
