class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        if book_title in self.books:
            self.books.remove(book_title)
            return True
        return False

    def search_book(self, keyword):
        keyword = keyword.casefold()
        return [book for book in self.books if keyword in book.casefold()]

    def display_books(self):
        print(f"Books in {self.name}:")
        if not self.books:
            print("No books in the collection.")
            return

        for book in self.books:
            print(book)


if __name__ == "__main__":
    library = Library("Central Library")
    library.add_book("The Python Handbook")
    library.add_book("Learning Data Structures")
    library.add_book("Python for Beginners")

    library.display_books()
    print("Search results:", library.search_book("python"))

    library.remove_book("Learning Data Structures")
    print("After removing a book:")
    library.display_books()