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
        

nov = Novel("J.K Rowling","Harry Potter")
nov.print_book()