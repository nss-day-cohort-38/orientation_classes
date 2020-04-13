class Library:
    def __init__(self, name):
        self.name = name
        self.books = list()

    def set_address(self, address):
        self.address = address
        
    def list_books(self):
        for book in self.books:
            # book.start_reading()
            print(f"Title: {book.title}, Author: {book.author}")
    
    def add_book(self, new_book):
        self.books.append(new_book)
