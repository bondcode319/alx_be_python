class Book:
    """Base class representing a book."""
   
    def __init__(self, title, author):
        """
        Initialize a Book instance.
       
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
    
    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
   
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook instance.
       
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): The file size in KB
        """
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """Return a string representation of the ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book."""
   
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook instance.
       
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): The number of pages
        """
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """Return a string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class representing a library that manages a collection of books."""
   
    def __init__(self):
        """Initialize a Library instance with an empty collection of books."""
        self.books = []
   
    def add_book(self, book):
        """
        Add a book to the library.
       
        Args:
            book: An instance of Book, EBook, or PrintBook
        """
        self.books.append(book)
   
    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(str(book))


# Example usage and testing
if __name__ == "__main__":
    # Create library instance
    library = Library()
    
    # Create different types of books
    regular_book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    ebook = EBook("1984", "George Orwell", 512)
    print_book = PrintBook("To Kill a Mockingbird", "Harper Lee", 376)
    
    # Add books to library
    library.add_book(regular_book)
    library.add_book(ebook)
    library.add_book(print_book)
    
    # Test initialization by printing book details
    print("Testing book initialization:")
    print(f"Regular book - Title: {regular_book.title}, Author: {regular_book.author}")
    print(f"EBook - Title: {ebook.title}, Author: {ebook.author}, File Size: {ebook.file_size}KB")
    print(f"Print book - Title: {print_book.title}, Author: {print_book.author}, Page Count: {print_book.page_count}")
    
    print("\nLibrary contents:")
    library.list_books()