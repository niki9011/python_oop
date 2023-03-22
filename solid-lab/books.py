class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.books_library = []

    def store(self):
        for x in books:
            self.books_library.append(x)

class Library(Book):

    def __init__(self,author, title):
        super().__init__(author, title)

    def find_book(self):

        if a in self.books_library:
            return self.title


books = [Library("Niki", "ABS")]
a = Library("Niki", "ABS")


