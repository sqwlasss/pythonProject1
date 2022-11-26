class Library():
    def __init__(self,book_list = []):
        self.book_list = book_list

    def new_book(self,book):
        self.book_list.append(book)

    def remove_book(self,name): # book is the name of the book
        for book in self.book_list:
            if book.name == name:
                self.book_list.remove(book)
                break


    def print_books(self):
        for book in self.book_list:
            print(f"Book {book.name} by {book.author}")


class Book():
    def __init__(self,author,name):
        self.author = author
        self.name = name

    def print_book(self):
        print(f"{self.name} by {self.author}")




class Novel(Book):
    def __init__(self,author,name):
        Book.__init__(self,author,name)

    def display(self):
        print(f"The Novel {self.name}")
        # Novel stuff which isn't common in all books

class Comic(Book):
    def __init__(self,author,name):
        Book.__init__(self,author,name)

    def display(self):
        print(f"The comic book {self.name}")
        # Comic book stuff which isn't common in all books


my_lib = Library()
my_lib.new_book(Novel("J.K Rowling","Harry Potter"))
my_lib.new_book(Novel("Aryan Parekh","Stack"))

my_lib.remove_book("Stack")

my_lib.print_books()