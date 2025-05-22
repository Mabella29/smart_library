from book import Book
from library import Library

lib = Library("Test Library")
lib.add_book(Book("Unexpectedly Mine","Mimi", 2020))
lib.add_book(Book("Money","Gina", 2026))
lib.add_book(Book("To kill a mocking bird", "Harper Lee", 2018))
print("Library catalog: ")

for book in lib.list_books():
    print("\n", book)
    

found = lib.find_book("Unexpectedly mine")
print(found.borrow())  if found else print("Book not found")