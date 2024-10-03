class Book: 
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
        
    def checkout(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
        
    def return_book(self):
        if not self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
        
    def available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Library: 
    
    def __init__(self):
        self._books = []
    
    def add_book(self, book): 
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.available():
                book.checkout()
                return True
            return False
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.available():
                book.borrow()
                return True
            return False
    
    def list_available_books(self):
        available_books = [book for book in self._books if book.available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books available.")
    