# Something I see a lot, but you SHOULDN'T DO

from typing import List, Dict


class BookShelf:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f'<Bookshelf with {self.quantity} books>'

bookshelf = BookShelf(300)

class Book(BookShelf):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.name = name

# This makes no sense, because now you need to pass `quantity` to a single book:

# -- Composition over inheritance here --

# Inheritance: "A Book is a BookShelf"
# Composition: "A BookShelf has many Books"

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'<Book: {self.name}>'

class BookShelf:
    def __init__(self, books: Dict[int, Book]):
        self.books = books

    def __str__(self):
        return f'<Bookshelf with {len(self.books)} books>'

book1 = Book('Harry')
book2 = Book('Potter')


books = {
    0: book1,
    1: book2
}
print(BookShelf(books))
