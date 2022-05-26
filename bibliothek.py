book = []
book_index = 0
book1 = {
    'name': 'White Fang',
    'author': 'Jack London',
    'desc': 'The story begins before the wolf-dog hybrid is born, with two men and their sled dog team on a journey to deliver the coffin of Lord Alfred to a remote town named Fort McGurry in the higher area of the Yukon Territory. The men, Bill and Henry, are stalked by a large pack of starving wolves over the course of several days. Finally, after all of their dogs and Bill have been eaten, more teams find Henry escaping from the wolves; the wolf pack scatters when they hear the large group of people coming.'}
book2 = {'name': 'Harry Potter',
         'author': 'British author J. K. Rowling',
         'desc': 'the novels chronicle the lives of a young wizard, Harry Potter, and his friends Hermione Granger and Ron Weasley, all of whom are students at Hogwarts School of Witchcraft and Wizardry. The main story arc concerns Harrys struggle against Lord Voldemort, a dark wizard who intends to become immortal, overthrow the wizard governing body known as the Ministry of Magic and subjugate all wizards and Muggles (non-magical people).'}
book3 = {
    'name': 'William Wenton și Hoțul de Luridium',
    'author': 'Bobbie Peers',
    'desc': 'William s-a intrebat mereu de ce familia sa si-a schimbat in mod neasteptat numele si adresa in urma cu opt ani, parasind Anglia pentru a se muta in Norvegia. Si ii e foarte dor de bunicul lui care a disparut in mod misterios chiar in aceeasi perioada. Abia dupa ce William reuseste sa decripteze Imposibilitatea, cel mai dificil cod din lume, isi da seama de pericolul care-l pandise din umbra in toti acesti ani. Pentru a supravietui, trebuie neaparat sa-si gaseasca bunicul cat mai repede si sa se foloseasca la maximum de talentul sau de spargator de coduri.'}
book4 = {
    'name': 'Twenty Thousand Leagues Under the Seas',
    'auth': 'Jules Verne',
    'desc': 'During the year 1866, ships of various nationalities sight a mysterious sea monster, which, it is later suggested, might be a gigantic narwhal.  The U.S. government assembles an expedition in New York City to find and destroy the monster. Professor Pierre Aronnax, a French marine biologist and the storys narrator, is in town at the time and receives a last-minute invitation to join the expedition; he accepts. Canadian whaler and master harpooner Ned Land and Aronnaxs faithful manservant Conseil are also among the participants.'}
'''buy_books = []
buy_books_index = 0
buy_books.append({'*'})
'''
cycle1 = True
choosen_of_thebook = False
person = []
person_index = 0
person.append({'email': 'scebec.cristian@gmail.com', 'pass': '123321', 'balance': '65000'})
person.append({'email': 'mpakaboy@gmail.com', 'pass': 'idontknow', 'balance': '53400'})
cycle = True
is_logg_in = False

personss = [name['email'] for name in person]


def loggin_in():
    global loggin_in
    username = input("Please enter your email: ")
    if not username in personss:
        print('Wrong email')
        loggin_in()
        passc = input('input your password')
        person_pass = None
        for x in person:
            if username == x['email']:
                person_pass == x['pass']
        if not passc == ['pass']:
            print('wrong pass')
            loggin_in()
        is_logg_in = True


def process_view_balance():
    global person_index
    print(f"Your balance is: {person[person_index]['balance']}")


books = [name['name'] for name in book]


def search_a_book():
    global person_index
    books = input('Search for the book.. ')
    if not book in books:
        print('we are sorry we dont have this book in our stock! ')
        print('choose a book from this list ')

        def list_of_books():
            global cycle1
            print('1. Choose an option')
            print('2. White Fang: Myth of the White Wolf by David Fallon')
            print('3. To Paradise by Hanya Yanagihara')
            print('4. Trust by Hernan Diaz')
            print('5. Fluturi by Irina Binder')
            print('0. Exit')
            abc = input('your choose of the book')
            if abc == 1:
                print('Your option: \n White Fang: Myth of the White Wolf, cost:500')
            elif abc == 2:
                print('Your option: \n To Paradise by Hanya Yanagihara, cost:780')
            elif abc == 3:
                print('Your option: \n Trust by Hernan Diaz, cost:1099')
            elif abc == 4:
                print('Your option: \n Fluturi by Irina Binder, cost:1209')
            elif abc == 0:
                cycle1 = False
            else:
                print('Wrong command')

        list_of_books()
        if book in books:
            choosen_of_thebook = True
        search_a_book()

def buy_a_book():
    print('First choose one of this avaible books =D')
    print('1. White Fang, cost:500')
    print('2. Harry Potter, cost:780')
    print('3. William Wenton și Hoțul de Luridium, cost:1099')
    print('4. Twenty Thousand Leagues Under the Seas, cost:1209')
    abcde1 = input('Choose a number 1-4 to buy that book')
    if abcde1 == 1:
        person[person_index]['balance'] - 500
    elif abcde1 == 2:
        person[person_index]['balance'] - 780
    elif abcde1 == 3:
        person[person_index]['balance'] - 1099
    elif abcde1 == 4:
        person[person_index]['balance'] - 1209

def view_a_book():
    print('1. White Fang')
    print('2. Harry Potter')
    print('3. William Wenton și Hoțul de Luridium')
    print('4. Twenty Thousand Leagues Under the Seas')
    abcde = input('Choose a number 1-4 to view information of that book')
    if abcde == 1:
        print(book1['name']), print(book1['author']), print(book1['desc'])
    if abcde == 2:
        print(book2['name']), print(book2['author']), print(book3['desc'])
    if abcde == 3:
        print(book3['name']), print(book3['author']), print(book3['desc'])
    if abcde == 4:
        print(book4['name']), print(book4['author']), print(book4['desc'])


def process_menu():
    global cycle
    print('Please choose an option: ')
    print('1. Search a book ')
    print('2. Buy a book')
    print('3. View balance')
    print('4. View a book from current bibliothek')
    inpp = int(input('choose one'))
    if inpp == 1:
        search_a_book()
    elif inpp == 3:
        process_view_balance()
    elif inpp == 4:
        view_a_book()

while (cycle):
    if not is_logg_in:
        loggin_in()
    process_menu()
