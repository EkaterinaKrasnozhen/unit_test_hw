import unittest
from unittest.mock import Mock

from book_service import BookService


class TestBookService(unittest.TestCase):
    def setUp(self) -> None:
        self.book_service = BookService(Mock())

    def test_get_book(self):
        book_id = 1
        self.book_service.find_book(book_id)
        self.book_service._book_repo.get_book.assert_called_with(book_id)

    def test_get_book_by_public_date(self):
        public_date = '1980'
        self.book_service.find_books_by_public_date(public_date)
        self.book_service._book_repo.get_book_by_public_date.assert_called_with(
            public_date)


if __name__ == '__main__':
    unittest.main()
