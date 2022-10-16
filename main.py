# This is a sample Python script
from pathlib import Path


class Book:
    def __init__(self, n, score):
        self.n = int(n)
        self.score = int(score)

    def __repr__(self):
        return f'Book #{self.n:05d} ({self.score:03d})'

class Library:
    N = 0

    def __init__(self, info_line_1, info_line_2):
        self.id = self.N
        self.N += 1

        self.n, self.t, self.m = (int(x) for x in info_line_1.split(' '))
        self.books = [int(x) for x in info_line_2.split(' ')]

    def __repr__(self):
        return (f"Library {self.id}: has {self.n} books, registers in {self.t} days, ships {self.m} books/day\n"
                f"\tBooks: {', '.join(str(x) for x in self.books)}")


class LibraryReader:

    def __init__(self):
        with Path('input.txt').open() as f:
            self.b, self.lib, self.n_days = (int(x) for x in f.readline().split(' '))

            self.books = [Book(i, x) for i, x in enumerate(f.readline().split(' '))]

            self.libraries = []

            for n_lib in range(self.lib):
                self.libraries.append(Library(f.readline(), f.readline()))

    def __call__(self, *args, **kwargs):
        print(self)

        print('AL lio')

    def __repr__(self):
        lib_sep = '\n\t'
        return (f'Books: we have {self.b} books, {self.lib} libraries and {self.n_days} days.\n'
                f'The books are: {lib_sep}{", ".join(str(x) for x in self.books)}\n'
                f'The following libraries are registered:{lib_sep}'
                f'{lib_sep.join(str(x) for x in self.libraries)}')


if __name__ == '__main__':
    LibraryReader()()
