from .book import Book


class PhysicalBook(Book):
    def __init__(
        self,
        title: str,
        author: str,
        isbn: int,
        is_borrowed: bool = False
    ) -> None:
        super().__init__(title, author, isbn)
        self.is_borrowed = is_borrowed

    def borrow(self) -> None:
        self.is_borrowed = True

    def drop(self) -> None:
        self.is_borrowed = False

    def __str__(self) -> str:
        status = "Unavailable" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} is {status}."

    def __repr__(self) -> str:
        return f"PhysicalBook(\"{self.title}\", \"{self.author}\", {self.isbn}, {self.is_borrowed})"
