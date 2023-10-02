from book_repository import BookRepository


class BookService:
    def __init__(self, book_repo: BookRepository):
        self._book_repo = book_repo

    def get_book_repository(self):
        return self._book_repo

    def find_book(self, book_id: int):
        return self._book_repo.get_book(book_id)

    def find_books_by_public_date(self, public_date: str):
        self._book_repo.get_book_by_public_date(public_date)
