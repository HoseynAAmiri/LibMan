class Book:
    def __init__(
        self,
        title: str,
        author: str,
        isbn: int
    ) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        return f"{self.title} by {self.author}."

    def __repr__(self) -> str:
        return f"Book(\"{self.title}\", \"{self.author}\", {self.isbn})"
