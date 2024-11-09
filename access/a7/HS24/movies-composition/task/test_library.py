#!/usr/bin/env python3

from unittest import TestCase
from movie import Movie
from moviebox import MovieBox
from library import Library


class LibraryTest(TestCase):
    def test_repr_movie(self):
        actual = repr(Movie("T", ["A", "B"], 123))
        expected = 'Movie("T", ["A", "B"], 123)'
        self.assertEqual(expected, actual)

    def test_repr_moviebox(self):
        actual = repr(MovieBox("T", [Movie("T2", ["A", "B"], 234)]))
        expected = 'MovieBox("T", [Movie("T2", ["A", "B"], 234)])'
        self.assertEqual(expected, actual)

    def test_str_movie(self):
        actual = str(Movie("T", ["A", "B"], 123))
        expected = "Title = T, Actors = ['A', 'B'], Duration = 123"
        self.assertEqual(expected, actual)

    def test_str_moviebox(self):
        actual = str(MovieBox("T", [Movie("T2", ["A", "B"], 234)]))
        expected = 'MovieBox = T, Movies = [[Movie("T2", ["A", "B"], 234)]]'
        self.assertEqual(expected, actual)

    def test_library(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino"], 175)
        c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
        d = MovieBox("Top Movies", [b, c])
        l = Library()
        l.add_movie(a)
        l.add_movie(d)
        self.assertEqual(413, l.get_total_duration())

    def test_empty_movie_title(self):
        with self.assertRaises(Warning):
            Movie("", ["Actor"], 120)

    def test_empty_movie_actors(self):
        with self.assertRaises(Warning):
            Movie("Title", [], 120)

    def test_invalid_movie_duration(self):
        with self.assertRaises(Warning):
            Movie("Title", ["Actor"], 0)

    def test_empty_moviebox_title(self):
        with self.assertRaises(Warning):
            MovieBox("", [Movie("Title", ["Actor"], 120)])

    def test_empty_moviebox_movies(self):
        with self.assertRaises(Warning):
            MovieBox("Title", [])

    def test_invalid_moviebox_content(self):
        with self.assertRaises(Warning):
            MovieBox("Title", ["Not a Movie"])

    def test_moviebox_get_actors(self):
        movie1 = Movie("Title1", ["Actor1", "Actor2"], 120)
        movie2 = Movie("Title2", ["Actor2", "Actor3"], 150)
        moviebox = MovieBox("Box", [movie1, movie2])
        self.assertEqual(moviebox.get_actors(), ["Actor1", "Actor2", "Actor3"])

    def test_moviebox_get_duration(self):
        movie1 = Movie("Title1", ["Actor1", "Actor2"], 120)
        movie2 = Movie("Title2", ["Actor2", "Actor3"], 150)
        moviebox = MovieBox("Box", [movie1, movie2])
        self.assertEqual(moviebox.get_duration(), 270)

    def test_library_no_duplicates(self):
        movie = Movie("Title", ["Actor"], 120)
        library = Library()
        library.add_movie(movie)
        library.add_movie(movie)
        self.assertEqual(len(library.get_movies()), 1)

    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
