class Book:
    def __init__(self, title, author, publication_date, ISBN, copies_available):
        self.title = title
        self.author = author  # Author object
        self.publication_date = publication_date
        self.ISBN = ISBN
        self.copies_available = copies_available
    
    def reserve_copy(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            return True
        return False
    
    def return_copy(self):
        self.copies_available += 1


class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography
        self.books = []  # List of Book objects
    
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, book):
        self.books.remove(book)


class Patron:
    def __init__(self, name, address, phone_number, email_address):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email_address = email_address
        self.borrowed_books = []  # List of borrowed Book objects
    
    def borrow_book(self, book):
        if book.reserve_copy():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print("Book not available.")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_copy()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print("This book was not borrowed by this patron.")


class TextBook(Book):
    def __init__(self, title, author, publication_date, ISBN, copies_available, subject):
        super().__init__(title, author, publication_date, ISBN, copies_available)
        self.subject = subject
    
    def get_subject(self):
        return self.subject


class ReferenceBook(Book):
    def __init__(self, title, author, publication_date, ISBN, copies_available, reference_section):
        super().__init__(title, author, publication_date, ISBN, copies_available)
        self.reference_section = reference_section
    
    def get_reference_section(self):
        return self.reference_section


# Example Usage
author1 = Author("J.K. Rowling", "Famous for the Harry Potter series.")
book1 = Book("Harry Potter", author1, "1997", "123456789", 5)
author1.add_book(book1)

patron1 = Patron("John Doe", "123 Street", "1234567890", "john@example.com")
patron1.borrow_book(book1)
patron1.return_book(book1)
