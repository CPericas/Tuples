#Task 1: Library System Enhancement
#Sharpen your skills in managing and modifying data within tuples and lists.
#Problem Statement:
#You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding 
# new books and ensuring no duplicates.
#Existing Library Data:
#library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
#Add functionality to insert new books into library.
#Ensure that adding a duplicate book is handled appropriately.

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library):
    while True:
        book_title = input("Name of book to add: ")
        author = input("Name of the author of the book being added: ")
        for title, writer in library:
            if title == book_title:
                print("This book already exists in the library.")
                print(library)
                return
        library.append((book_title, author))
        print("Book added successfully!")
        print(library)
        another_entry = input("Would you like to add another book to the Library? (y / n): ").lower()
        if another_entry != "y":
            break

add_book(library)

