from book import Book

class DigitalBook(Book):
    def __init__(self, title, author, year):
        super().__init__(title, author, year)
