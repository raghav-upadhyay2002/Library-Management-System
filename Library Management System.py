class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def search_book(self, title):
        found_books = []
        for book in self.books:
            if title.lower() in book.title.lower():
                found_books.append(book)
        return found_books

    def borrow_book(self, book):
        if book.available:
            book.available = False
            print(f"You have borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book):
        if not book.available:
            book.available = True
            print(f"You have returned '{book.title}'.")
        else:
            print(f"'{book.title}' is already available.")


# Usage example:
library = Library()

book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "978-0747532699")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")
book3 = Book("1984", "George Orwell", "978-0451524935")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Searching for books
search_title = "harry potter"
found_books = library.search_book(search_title)
if found_books:
    print(f"Found {len(found_books)} book(s) with '{search_title}' in the title:")
    for book in found_books:
        print(book)
else:
    print("No books found.")

# Borrowing a book
library.borrow_book(book1)

# Returning a book
library.return_book(book1)
