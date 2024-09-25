from .book import Book


class EBook(Book):
    def __init__(self, title: str, author: str, isbn: int, link: str) -> None:
        super().__init__(title, author, isbn)
        self.link = link

    def __str__(self) -> str:
        return f"{self.title} by {self.author} at {self.link}."

    def __repr__(self) -> str:
        return f"EBook(\"{self.title}\", \"{self.author}\", {self.isbn}, \"{self.link}\")"
