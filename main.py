from LibMan import Member, Library
from LibMan.data import *


hoseyn = Member("Hoseyn", 1, [])
book_list = [book1, book2, book3, book4, book5]
library = Library(books=book_list)

library.register_member(hoseyn)
library.borrow_book(hoseyn.member_id, 111111)
library.borrow_book(hoseyn.member_id, 555555)
library.borrow_book(hoseyn.member_id, 666666)

print(library.list_members())
print(library.list_books())

library.drop_book(hoseyn.member_id, 555555)
print(library.list_members())
print(library.list_books())
