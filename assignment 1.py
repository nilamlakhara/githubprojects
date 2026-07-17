class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available=True

class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books =[]

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []
    def add_book(self, title, author):
        new_book = Book(title, author)
        self.patrons.append(new_book)
    def register_patron(self, name):
        new_patron = Patron(name)
        self.patrons.append(new_patron)
    def issue_book(self, title, patron_name):
        for book in self.books:
            if book.title == title and book.is_available:
                for patron in self.patrons:
                    if patron.name == patrom_name:
                        book.is_available = False
                        patron.borrowed_books.append(book)
                        return f"{title} has been issued to {patron_name}."
        return "Book is not available or patron not found."
    def return_book(self, title, patron_name):
        for patron in self.patrons:
            if patron.name == patron_name:
                for book in patron.borrowed_books:
                    if book.title == title:
                        book.is_available = True
                        patron.borrowed_books.remove(book)
                        return f"{title} has been returned ny {patron_name}."
        return "Book not found in patrons's records."  