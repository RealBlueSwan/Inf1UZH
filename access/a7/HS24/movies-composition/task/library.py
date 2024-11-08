#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from movie import Movie
from moviebox import MovieBox


class Library:
    def __init__(self):
        self._movielist = []

    def add_movie(self, movie: Movie):
        if movie not in self._movielist:
            self._movielist.append(movie)

    def get_movies(self) -> list:
        movies = []
        seen_titles = set()
        
        def collect_movies(item):
            if isinstance(item, Movie):
                if item.get_title() not in seen_titles:
                    seen_titles.add(item.get_title())
                    movies.append(item)
            elif isinstance(item, MovieBox):
                for movie in item.get_movies():
                    collect_movies(movie)
        
        for item in self._movielist:
            collect_movies(item)
        
        return sorted(movies, key=lambda m: m.get_title())

    def get_total_duration(self) -> int:
        duration = 0
        for m in self._movielist:
            if isinstance(m, Movie):
                duration += m.get_duration()
            elif isinstance(m, MovieBox):
                duration += m.get_duration()
        return duration