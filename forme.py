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

'''    money = 500
    money1 = 780
    money2 = 1099
    money3 = 1209


    if abcdee == 1:
        print('warning you cant buy a book witch costs more than your balance')
        if money > person['balance']:
            print('you cant buy a book which costs more than your balance, exiting...')
            time.sleep(0.6)
            exit()
        elif money <= person['balance']:
            print('well, you can buy =D')
            time.sleep(0.9)
            person['balance'] = person['balance'] - money
            time.sleep(1)
            print('succesefuly bought')
    elif abcdee == 2:
        print('warning you cant buy a book witch costs more than your balance')
        x = person.get('balance')
        if money1 > person['balance']:
            print('you cant buy a book which costs more than your balance, exiting...')
            time.sleep(0.6)
            exit()
        elif money1 <= person['balance']:
            print('well, you can buy =D')
            time.sleep(0.9)
            person['balance'] = person['balance'] - money1
            time.sleep(1)
            print('succesefuly bought')
    elif abcdee == 3:
        print('warning you cant buy a book witch costs more than your balance')
        x = person.get('balance')
        if money2 > person['balance']:
            print('you cant buy a book which costs more than your balance, exiting...')
            time.sleep(0.6)
            exit()
        elif money2 <= person['balance']:
            print('well, you can buy =D')
            time.sleep(0.9)
            person['balance'] = person['balance'] - money2
            time.sleep(1)
            print('succesefuly bought')
    elif abcdee == 4:
        print('warning you cant buy a book witch costs more than your balance')
        x = person.get('balance')
        if money3 > person['balance']:
            print('you cant buy a book which costs more than your balance, exiting...')
            time.sleep(0.6)
            exit()
        elif money3 <= person['balance']:
            print('well, you can buy =D')
            time.sleep(0.9)
            person['balance'] = person['balance'] - money3
            time.sleep(1)
            print('succesefuly bought')'''