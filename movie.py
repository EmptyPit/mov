#!/usr/bin/env python3

import pdb
import argparse
import sys
import difflib


class MovieFactory(object):
    DELIM = ';'

    def __init__(self, input_file):
        self._in_f = input_file
        self.header = self._get_header()
        self.raw_lines = self._get_raw_lines()

    def _get_header(self):
        with open(self._in_f, "r", encoding='ISO-8859-1') as f:
            return tuple(f.readline().strip('\n').split(self.DELIM))

    def _get_raw_lines(self):
        with open(self._in_f, "r", encoding='ISO-8859-1') as f:
            lines = [line.strip('\n') for line in f.readlines()[2:]]

        return lines

    def process(self):
        preprocessed = []
        for line in self.raw_lines:
            preprocessed.append(Movie(**self._raw_to_dict(line)))

        return preprocessed

    def _raw_to_dict(self, line):
        return dict(zip(self.header, line.split(self.DELIM)))

    def search_mov(self, title):
        """
        Searches for a movie title and returns the result
        :return:
        """
        list1 = []
        for i in self.process():
            if title in  i.title:
                list1.append(i)
            elif i.title != title:
                v = difflib.SequenceMatcher(None, i.title, title).ratio()
                if v > 0.50:
                    list1.append(i)
        print(', '.join(repr(e) for e in list1))

    def search_year(self, year):
        """Searches movies certain year and returns a list of such movies"""
        list_year = []
        for i in self.process():
            if year in i.year:
                list_year.append(i)
        print(','.join((repr(e) for e in list_year)))

class Movie(object):
    def __init__(self, **kwargs):

        self.year = kwargs["Year"]
        self.length = kwargs["Length"]
        self.title = kwargs["Title"]
        self.subject = kwargs["Subject"]
        self.actor = kwargs["Actor"]
        self.actress = kwargs["Actress"]
        self.director = kwargs["Director"]
        self.popularity = kwargs["Popularity"]
        self.awards = kwargs["Awards"]
        self.image = kwargs["*Image"]

    def __str__(self):
        return "Title -{} Year -{} Lenght -{}min\n".format(self.title, self.year, self.length)
    __repr__ = __str__


if __name__ == '__main__':
    fact = MovieFactory('film.csv')
    parser = argparse.ArgumentParser(description="Searches movie titles")
    parser.add_argument('-n', '--movie_name', help='Input movie title')
    parser.add_argument('-m', '--movie_year', help='Input movie year')
    args = parser.parse_args()
    if args.movie_name:
        x = fact.search_mov(args.movie_name)
        print(x)
    elif args.movie_year:
        y = fact.search_year(args.movie_year)
        print(y)
    # y = fact.search_year(args.movie_year)
    # x = fact.search_mov(args.movie_name)
    # print(x)


# print("Arguments from the terminal: {}".format(", ".join(["# %s=%s" % (i, a) for i, a in enumerate(sys.argv)])))
#encoding="ISO-8859-1"