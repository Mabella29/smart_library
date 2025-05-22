from digitalbook import DigitalBook

ebook = DigitalBook("Python for all", "Guido van Rossum",2020,75)

print(ebook.borrow())            # Overrides original method
print(ebook.get_details())       # Unique to digital books
print(ebook.stream())    

