class Book:
    """A class representing a book with magic methods implementation."""
    
    def __init__(self, title, author, year):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """Destructor method called when object is deleted."""
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        Return string representation for end users.
        
        Returns:
            str: Human-readable string representation
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Return official string representation for developers.
        
        Returns:
            str: String that can recreate the Book instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"