from . import PhysicalBook, Member


class Library:
    def __init__(
        self,
        books: list[PhysicalBook] = [],
        members: list[Member] = []
    ) -> None:
        self.books = books
        self.members = members

    def add_book(self, book: PhysicalBook) -> None:
        self.books.append(book)

    def remove_book(self, book: PhysicalBook) -> None:
        self.books.remove(book)

    def register_member(self, member: Member) -> None:
        self.members.append(member)

    def list_books(self) -> list[str]:
        return [str(book) for book in self.books]

    def list_members(self) -> list[str]:
        return [str(member) for member in self.members]

    def borrow_book(self, member_id: int, isbn: int) -> None:
        for member in self.members:
            if member_id == member.member_id:
                for book in self.books:
                    if isbn == book.isbn and not book.is_borrowed:
                        book.borrow()
                        member.borrow_book(book)

    def drop_book(self, member_id: int, isbn: int) -> None:
        for member in self.members:
            if member_id == member.member_id:
                for book in self.books:
                    if isbn == book.isbn and book.is_borrowed:
                        book.drop()
                        member.drop_book(book)
