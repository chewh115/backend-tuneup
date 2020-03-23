#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = """chewh115, baseline decorator function taken from demo notebook
                and modified to fit"""

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    @functools.wraps(func)
    def inner_wrapper(*args, **kwargs):
        # Do something before calling func_to_decorate
        result = func(*args, **kwargs)
        # Do something after calling func_to_decorate
        return result
    return inner_wrapper


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(stmt="find_duplicate_movies('movies.txt')",
                     setup="from __main__ import find_duplicate_movies")
    result = min(t.repeat(repeat=7, number=3))/3
    print(f'The best of 7 repeats with 3 runs per repeat: {result} seconds')


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    timeit_helper()
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
