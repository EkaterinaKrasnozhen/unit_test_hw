
from book import Book


class BookRepository:
    def __init__(self, book_repo: list[Book] = None):
        self._book_repo = book_repo
        if self._book_repo == None:
            self._book_repo = []

    def get_book(self, book_id: int):
        return [*filter(lambda x: x._book_id == book_id, self._book_repo)][0]

    def get_book_by_public_date(self, public_date: str):
        book_list = []
        for book in self._book_repo:
            if public_date in book._public_date:
                book_list.append(book)
        return book_list

    def add_book(self, book: Book):
        self._book_repo.append(book)

    def __iter__(self) -> str:
        for book in self._book_repo:
            return book
