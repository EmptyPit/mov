#!/usr/bin/env python3


class Movie (object):

    def __init__(self, title, way, items_from_csv):
        self.title = title
        self.way = way
        self.items_from_csv = items_from_csv

    def read_open (self):
        with open(self.way) as file_csv:
            items_from_csv = []
            sum(items_from_csv, [])
            for i in file_csv:
                #words = i.split(",")
                items_from_csv.append(i)
                #print(i)

    def find_movie_title(self):
        for i in self.items_from_csv:
            if i == self.title:
                print(i)
            else:
                break


mm = Movie("Octopussy", "/home/andrii/PycharmProjects/movie_parser/film.csv", items_from_csv=[])
mm.read_open()
mm.find_movie_title()

#"/home/andrii/PycharmProjects/movie_parser/film.csv"
#encoding="ISO-8859-1"