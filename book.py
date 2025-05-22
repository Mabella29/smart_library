# Book is an object have the below properties
# Think the init as the form you fill when you go to the library
# it stores all information about the book object
class Book:
    def __init__(self,title, author, year):
        """Constructor method to initialize the book object"""
        self.title = title
        self.author = author
        self.year = year
        self.available = True # Default to available
     
# if you borrow a book, it means it's not available
# Hence "False"   
    def borrow(self):
        """Marks the book has been borrowed if available"""
        if self.available:
            self.available = False
            return f"You have borrowed '{self.title}'."
        return f"'{self.title}' is currently Not available."
        

    def return_book(self):
        """
        Mark the book has returned
        """

        self.available = True
        return f"'{self.title}' has been returned."
    
    def get_details(self):
        """
        Returns book information
        """   
        return f"{self.title} by {self.author} {self.year}"
    
    
    
    # Book.get_details()
    # Book.available