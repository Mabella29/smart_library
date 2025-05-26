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
        self.__rating = 0
     
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


    def set_rating(self, rating):
        """
        Set rating from 0-5 for the book
        This is an example of encapsulation: rating is private
        """
        if 0<= 5:
            self.__rating = rating
        else:
            print(" Rating must be between 0 and 5")
            
            
    def get_rating(self):
        """
        Get the current rating of the book
        """
        return self.__rating
    
    # Book.get_details()
    # Book.available