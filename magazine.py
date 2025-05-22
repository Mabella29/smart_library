from book import Book

class Magazine(Book):
    def __init__(self, title, editor, year):
        # we still call the parent constructor, but use editor instead of author
        super().__init__(title, editor, year)
        
        
    def borrow(self):
        """Magazine can't be borrowed-overrides borrow method"""
        return f"{self.title} is a magazine and can't be borrowed"