import pandas as pd
import numpy as np


class BookLover:

    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre

    # method 1
    def add_book(self, new_book, book_name, book_rating):
        assert isinstance(book_name, str)
        assert isintance(book_rating, int)
        self.book_name = book_name
        self.book_rating = book_rating
        self.num_books_read += 1

    # method 2
    def has_read(self, book_name):
        if book_name in book_list:
            print("True")
        else:
            print("False")

    # method 3
    def num_books_read(self):
        return self.num_books

    # method 4
    def fav_books(self):
        print(self.book_list[self.book_list.book_rating > 3])

