class Book:
    def __init__(self, book_id: int, book_name: str, author: str, public_date: str):
        self._book_id = book_id
        self._book_name = book_name
        self._author = author
        self._public_date = public_date

    def __str__(self) -> str:
        return f'{self._book_name} {self._author} {self._public_date}'
