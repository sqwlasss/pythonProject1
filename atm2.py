users = []
user_index = 0
users.append({'username': 'mike', 'pin': '1234', "balance": 56000})
users.append({'username': 'cristy', 'pin': '1111', "balance": 7})
cycle = True
is_logged_in = False

usernames = [name['username'] for name in users]


def log_in():
    global is_logged_in
    username = input("Please enter your username: ")
    if not username in usernames:
        print('wrong username!')
        log_in()
    pin = input('Please enter your pin: ')
    users_pin = None
    for n in users:
        if username == n['username']:
            users_pin = n['pin']
    if not pin == users_pin:
        print('wrong pin!')
        log_in()
    is_logged_in = True


def process_view_balance():
    global user_index
    print(f"Your balance is: {users[user_index]['balance']}")


def process_withdraw():
    global user_index
    amount = int(input('Amount of cash to withdraw: '))
    if 0 <= amount <= users[user_index]['balance']:
        users[user_index]['balance'] -= amount
    else:
        print('wrong amount to withdraw')


def process_put_cash():
    global user_index
    amount = int(input('Amount of cash to add: '))
    if amount >= 0:
        users[user_index]['balance'] += amount
    else:
        print('wrong amount to put')


def process_menu():
    global cycle
    print('Please pick an option')
    print('1. View balance')
    print('2. Withdraw some amount')
    print('3. Put some amount')
    print('0. Exit')
    inp = int(input('Option: '))
    if inp == 1:
        process_view_balance()
    elif inp == 2:
        process_withdraw()
    elif inp == 3:
        process_put_cash()
    elif inp == 0:
        cycle = False
    else:
        print('Wrong command')


while (cycle):
    if not is_logged_in:
        log_in()
    process_menu()
