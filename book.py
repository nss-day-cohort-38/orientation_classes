class Book:
# All methods defined in a class need to have self as the first argument.
    def __init__(self, title, author):
        self.title = title
        self.current_page = 1
        self.author = author
        self.currently_reading = False

    def start_reading(self):
        self.currently_reading = True
        print(
            f"You started reading {self.title}, your current page is {self.current_page}.")

    def stop_reading(self, page):
        self.current_page = page
        
if __name__ == '__main__':
    print("Hello from the Book class")
