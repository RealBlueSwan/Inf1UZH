#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from movie import Movie


class MovieBox(Movie):
    def __init__(self, title: str, movies: list):
        if not title:
            raise Warning("Title is empty")
        if not movies:
            raise Warning("There are no movies in the box")
        for movie in movies:
            if not isinstance(movie, Movie):
                raise Warning("All items in the movie list must be of type Movie")
        super().__init__(title, [], sum(movie.get_duration() for movie in movies))
        self._movies = movies

    def __repr__(self):
        movies_str = ', '.join(repr(movie) for movie in self._movies)
        return f'MovieBox("{self._title}", [{movies_str}])'
    
    def __str__(self):
        return f"MovieBox = {self._title}, Movies = [{self._movies}]"

    def __eq__(self, other):
        if not isinstance(other, MovieBox):
            return False
        return (self._title == other._title and self._movies == other._movies)

    def __hash__(self):
        return hash((self._title, tuple(self._movies)))

    def get_title(self):
        return self._title

    def get_actors(self):
        actor_list = []
        for movie in self._movies:
            actor_list.extend(movie.get_actors())
        return sorted(list(set(actor_list)))
        
    def get_duration(self):
        return sum(movie.get_duration() for movie in self._movies)

    def get_movies(self):
        return self._movies.copy()