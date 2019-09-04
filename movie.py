#!/usr/bin/env python3

import argparse


class MovieFactory(object):
    DELIM = ';'
    AFTER_PROCES_LIST = []

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
        for line in self.raw_lines:
            self.AFTER_PROCES_LIST.append(Movie(**self._raw_to_dict(line)))

        return self.AFTER_PROCES_LIST

    def _raw_to_dict(self, line):
        return dict(zip(self.header, line.split(self.DELIM)))

    # def search_mov(self, title):
    #     """
    #     Searches for a movie title and returns the result
    #     :return:
    #     """
    #     list1 = []
    #     for i in self.process():
    #         if title in i.title:
    #             list1.append(i)
    #     print(list1)
    #     # print(', '.join(repr(e) for e in list1))

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
        return "Title {}...\t\t\t\tYear {}\t\tLenght {}".format(self.title, self.year, self.length)
    __repr__ = __str__

class Filter(object):
    def __init__(self, after_process_list):
        self.after_list = after_process_list

    def get_filtered(self):
        return self.after_list

    def filter_by_name(self, title):
        self.after_list = [i for i in self.after_list if title in i.title]

        return self

    def filter_by_year(self, year):
        self.after_list = [i for i in self.after_list if year == i.year]

        return self

    def filter_by_lenght(self, length):
        self.after_list = [i for i in self.after_list if length == i.length]

        return self


def display(movies, params):
    p = (('Len', 'title', 30), ('Name', 'year', 4), ('Year', 'length', 6))

    headers = tuple([i[0] for i in p])
    field_names = tuple([i[1] for i in p])
    matrix = [headers]

    for i, m in enumerate(movies):
        tmp = [getattr(m, n) for n in field_names]
        tmp.insert(0, i)
        matrix.append(tmp)

    return matrix


def sorted_output(movies):
    width = [30, 5, 4]
    list_1 = []
    for movie in movies:
        list_2 = []
        for e, i in enumerate(movie[1:]):
            if len(i) < width[e]:
                i = "{:{width}}".format(i, width=width[e])
                list_2.append(i)
            elif len(i) > width[e]:
                list_2.append(i[:width[e]])
        list_1.append(list_2)

    for i in list_1:
        print(" | ".join(i))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Searches movie titles")
    parser.add_argument('-n', '--movie_name', help='Input movie title')
    parser.add_argument('-y', '--movie_year', help='Input movie year')
    parser.add_argument('-l', '--movie_lenght', help='Input movie lenght')
    args = parser.parse_args()
    fact = MovieFactory('film.csv')

    movies_db = fact.process()
    movie_filter = Filter(movies_db)

    if args.movie_name:
        movie_filter.filter_by_name(args.movie_name)
    if args.movie_lenght:
        movie_filter.filter_by_lenght(args.movie_lenght)
    if args.movie_year:
        movie_filter.filter_by_year(args.movie_year)

    mat = display(movie_filter.get_filtered(), None)
    output = sorted_output(mat)
    print(output)

    # print("\n ".join(str(x) for x in mat))


    # print(display(movie_filter.get_filtered(), None))

    # z = "\n".join(["%d: %s" % (i, str(m)) for i, m in enumerate(movie_filter.get_filtered())])
    # new_line = z.replace("Title", "").replace("Year", "").replace("Lenght", "")
    # h = head(z)

    # header_map1 = [["Title", "title"], ["Year", "year"], ["Lenght", "length"]]
    # print(header_map1)

    # if args.movie_name and args.movie_year:
    #     print(Filter(fact.process()).filter_by_name(args.movie_name).filter_by_year(args.movie_year).get_filtered())
    # elif args.movie_name and args.movie_lenght:
    #     print(Filter(fact.process()).filter_by_name(args.movie_name).filter_by_lenght(args.movie_lenght).get_filtered())

# print("Arguments from the terminal: {}".format(", ".join(["# %s=%s" % (i, a) for i, a in enumerate(sys.argv)])))
#encoding="ISO-8859-1"
