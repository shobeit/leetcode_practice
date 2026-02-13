class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        # We create a new list excluding the book with the matching title and author
        books_to_keep = []
        for b in self.books:
            if b.title != book.title or b.author != book.author:
                books_to_keep.append(b)
        self.books = books_to_keep

    def search_books(self, search_string):
        # Case-insensitive search across title and author
        results = []
        search_string = search_string.lower()
        for book in self.books:
            if search_string in book.title.lower() or search_string in book.author.lower():
                results.append(book)
        return results