# combining all together(polymorphism)

from library import Library
from book import Book
from magazine import Magazine
from digitalbook import DigitalBook

def main():
    library = Library("smart city library")
    
    # Add Various book types to the library
    library.add_book(Book("Unexpectedly Mine","Mimi", 2020))
    library.add_book(DigitalBook("Money","Gina", 2026, 70))
    library.add_book(Magazine("To kill a mocking bird", "Harper Lee", 2018))
    
    
    while True:
        print("\n Welcome to the smart library")
        print("1. View All Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Rate a Book")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice =="1":
            print("\n Library Catalog: ")
            for book in library.books:
                print("-",book.get_details())
                
        elif choice == "2":
            title = input("Enter the title of the book you want to borrow: ")
            book = library.find_book(title)
            if book:
                print(book.borrow())  #polymorphism: each book behaves differently
                
            else:
                print("Book not found")
                
        elif choice == "3":
            title = input("Enter the title of the book you want to return: ")
            book = library.find_book(title)
            if book:
                print(book.return_book())  
                
            else:
                print("Book not found")
                
        elif choice == "4":
            title = input("Enter the title of the book you want to rate: ")
            book = library.find_book(title)
            if book:
                try:
                    rating = int(input("Enter a rating from 0-5: "))
                    book.set_rating(rating)
                    print(f"Thanks! Current rating: {book.get_rating()}/5")
                    
                except ValueError:
                    print("Invalid Input. Please enter a number")
                    
            else:
                print("Book not found")
            
        elif choice == "5":
            print("Exiting Smart Library.See you again!")
            break
        
        else:
            print("Invalid choice. Please try again.")
            
            
if __name__ == "__main__":
    main()
        
    