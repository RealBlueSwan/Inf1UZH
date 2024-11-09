#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

class Movie:
    def __init__(self, title: str, actors: list, duration: int):
        if not title:
            raise Warning("Title is empty")
        if not actors and self.__class__.__name__ != 'MovieBox':
            raise Warning("Actors list is empty")
        if duration < 1:
            raise Warning("Duration must be at least 1 minute")
        self._title = title
        self._actors = actors
        self._duration = duration

    def __repr__(self) -> str:
        actors_str = ', '.join(f'"{actor}"' for actor in self._actors)
        return f'Movie("{self._title}", [{actors_str}], {self._duration})'
    
    def __str__(self) -> str:
        return f"Title = {self._title}, Actors = {self._actors}, Duration = {self._duration}"
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Movie):
            return (self._title == other._title and self._actors == other._actors and self._duration == other._duration)
        return False
    
    def __hash__(self):
        return hash((self._title, tuple(self._actors), self._duration))

    def get_title(self) -> str:
        return self._title

    def get_actors(self) -> list:
        return self._actors
    
    def get_duration(self) -> int:
        return self._duration