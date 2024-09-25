from typing import Protocol


class Titled(Protocol):
    title: str


class Member:
    def __init__(
        self,
        name: str,
        member_id: int,
        borrowed_books: list[Titled]
    ) -> None:
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books

    def borrow_book(self, book: Titled) -> None:
        self.borrowed_books.append(book)

    def drop_book(self, book: Titled) -> None:
        self.borrowed_books.remove(book)

    def __str__(self) -> str:
        titles = [book.title for book in self.borrowed_books]
        return f"{self.name} borrowed {', '.join(titles)}."
