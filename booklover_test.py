import pandas as pd
from pandas._testing import assert_frame_equal
import unittest
import numpy as np
from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self, book_list=pd.DataFrame({'book_name': [], 'book_rating': []})):
        user1 = BookLover("Audrika", "audrikaindu@gmail.com", "Mystery")
        self.book_list = book_list
        new_book1 = pd.DataFrame({'book_name': ['A Thousand Splendid Suns'], 'book_rating': [4]})
        self.book_list = pd.concat([book_list, new_book1], ignore_index=True)


    def test_2_add_book(self):
        new_book1 = pd.DataFrame({'book_name': ['A Thousand Splendid Suns'], 'book_rating': [4]})
        new_book2 = pd.DataFrame({'book_name': ['A Thousand Splendid Suns'], 'book_rating': [4]})
        msg = "This book has already been added!"
        assert_frame_equal(new_book1, new_book2, msg)

    def test_3_has_read(self):
        new_book1 = pd.DataFrame({'book_name': ['A Thousand Splendid Suns'], 'book_rating': [4]})
        new_book3 = pd.DataFrame({'book_name': ['A Thousand Splendid Suns'], 'book_rating': [4]})
        msg = "This book has already been added!"
        assert_frame_equal(new_book1, new_book3, msg)


    def test_4_has_read(self):
        new_book1 = pd.DataFrame({'book_name': ['A Thousand Splendid Suns'], 'book_rating': [4]})
        new_book4 = pd.DataFrame({'book_name': ['The Popol Vuh'], 'book_rating': [5]})
        msg = "This book has not previously been read"
        np.array_equal(new_book1.values, new_book4.values)

    def test_5_num_books_read(self, book_list=pd.DataFrame({'book_name': [], 'book_rating': []})):
        self.book_list = book_list
        user1 = BookLover("Audrika", "audrikaindu@gmail.com", "Mystery")
        new_book2 = pd.DataFrame({'book_name': ['Jane Eyre'], 'book_rating': [4]})

        self.book_list = pd.concat([book_list, new_book2], ignore_index=True)

        self.num_books = len(self.book_list)
        # test
        expected = 1
        self.assertEqual(self.num_books, expected)

    def test_6_fav_books(self, book_list=pd.DataFrame({'book_name': [], 'book_rating': []})):
        self.book_list = book_list

        user1 = BookLover("Audrika", "audrikaindu@gmail.com", "Mystery")
        new_book1 = pd.DataFrame({'book_name': ['A Thousand Splendid Suns'], 'book_rating': [4]})
        self.book_list = pd.concat([book_list, new_book1], ignore_index=True)

        new_book2 = pd.DataFrame({'book_name': ['Jane Eyre'], 'book_rating': [4]})
        self.book_list = pd.concat([book_list, new_book2], ignore_index=True)

        new_book3 = pd.DataFrame({'book_name': ['Stolen'], 'book_rating': [3]})
        self.book_list = pd.concat([book_list, new_book3], ignore_index=True)

        print(self.book_list[self.book_list.book_rating > 3])


if __name__ == '__main__':
    unittest.main(verbosity=3)
