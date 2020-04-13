from book import Book
from library import Library

# Creating an instance of class Book.
# Because the __init_method specifies that two arguments are required, we pass them in on instantiation.
book_one = Book("Harry Potter and the Sorcerer's Stone", "J K Rowling")
print("Book One:")
print(type(book_one))
#Dot notation allows you to access all properties and methods on an instance.
print(book_one.title)
print(book_one.current_page)
print(book_one.author)

book_one.start_reading()

book_one.stop_reading(55)
print(book_one.current_page)

book_one.start_reading()

book_two = Book("Harry Potter and the Chamber of Secrets", "J K Rowling")
print("Book Two:")
print(type(book_two))
print(book_two.title)
print(book_two.current_page)
print(book_two.author)

print("*********************************************")

my_library = Library("My Personal Library")

print(type(my_library))
my_library.add_book(book_one)
print("List of books: ")
my_library.list_books()

# This conditional only evaluates to true if this is file that is excuted ie, `python main.py` from command line.
if __name__ == '__main__':
    print("Hello main file being executed!")
