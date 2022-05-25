book = []
book_index = 0
book.append({'name': 'White Fang', 'author': ' Jack London',
             'desc': 'The story begins before the wolf-dog hybrid is born, with two men and their sled dog team on a journey to deliver the coffin of Lord Alfred to a remote town named Fort McGurry in the higher area of the Yukon Territory. The men, Bill and Henry, are stalked by a large pack of starving wolves over the course of several days. Finally, after all of their dogs and Bill have been eaten, more teams find Henry escaping from the wolves; the wolf pack scatters when they hear the large group of people coming.'})
book.append({'name': 'Harry Potter', 'author': 'British author J. K. Rowling',
             'desc': 'the novels chronicle the lives of a young wizard, Harry Potter, and his friends Hermione Granger and Ron Weasley, all of whom are students at Hogwarts School of Witchcraft and Wizardry. The main story arc concerns Harrys struggle against Lord Voldemort, a dark wizard who intends to become immortal, overthrow the wizard governing body known as the Ministry of Magic and subjugate all wizards and Muggles (non-magical people).'})
book.append({'name': 'William Wenton și Hoțul de Luridium', 'author': 'Bobbie Peers',
             'desc': 'William s-a intrebat mereu de ce familia sa si-a schimbat in mod neasteptat numele si adresa in urma cu opt ani, parasind Anglia pentru a se muta in Norvegia. Si ii e foarte dor de bunicul lui care a disparut in mod misterios chiar in aceeasi perioada. Abia dupa ce William reuseste sa decripteze Imposibilitatea, cel mai dificil cod din lume, isi da seama de pericolul care-l pandise din umbra in toti acesti ani. Pentru a supravietui, trebuie neaparat sa-si gaseasca bunicul cat mai repede si sa se foloseasca la maximum de talentul sau de spargator de coduri.'})
book.append({'name': 'Twenty Thousand Leagues Under the Seas', 'auth': 'Jules Verne',
             'desc': 'During the year 1866, ships of various nationalities sight a mysterious sea monster, which, it is later suggested, might be a gigantic narwhal. The U.S. government assembles an expedition in New York City to find and destroy the monster. Professor Pierre Aronnax, a French marine biologist and the storys narrator, is in town at the time and receives a last-minute invitation to join the expedition; he accepts. Canadian whaler and master harpooner Ned Land and Aronnaxs faithful manservant Conseil are also among the participants.'})
buy_books = []
buy_books_index = 0
buy_books.append({'*'})
cycle1 = True
person = []
person_index = 0
person.append({'email': 'scebec.cristian@gmail.com', 'pass': '123321', 'balance': '65000'})
person.append({'email': 'mpakaboy@gmail.com', 'pass': 'idontknow', 'balance': '53400'})
cycle = True
is_logg_in = False

personss = [name['email'] for name in person]


def loggin_in():
    global loggin_in
    username = input("Please enter your username: ")
    if not username in personss:
        print('Wrong email')
        loggin_in
        passc = input('input your password')
        person_pass = None
        for x in person:
            if username == x['email']:
                person_pass == x['pass']
            if not passc == ['pass']:
                print('wrong pass')
                loggin_in()


is_logg_in = True

def search():
    global person_index
    input('Search your book . . . ')
    search()

books = [name['book'] for name in buy_books]

def buy_a_book():
    global person_index
    bbok = input('Search for the book.. ')
    if not book in books:
        print('we are sorry we dont have this book in our stock! ')
        buy_a_book()
        if book in books:
            input('choose a book from this list ')
            buy_a_book()




def process_menu():
    global cycle
    print('Please choose an option: ')
    print('1. Search a book ')
    print('2. Buy a book')
    inpp = int(input('choose one'))
    if inpp == 1:
        search()
    if inpp == 2:
        print




