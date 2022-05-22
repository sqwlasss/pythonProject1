import random
import time

dictionary = {
    "02001":{
   'name1' : 'cristy',
   'passw' : '0808',
   'money' : 777,
   "status": 0
}
}
dictionary1 = {
   'name1' : 'cristy',
   'passw' : '0808',
   'money' : 208082008,
    'pin' : '02001'
}

client = []
#client.append('person')
person = {
    "name": "cristy",
    "PIN": '0201'
}
#PIN = 2001
def logging():
    a = input("write your name please:")
    b = input("PIN:")
    if a == person["name"]:
        pass
    elif a != person["name"]:
        exit()
        if b == person["PIN"]:
            pass
        elif b != person["PIN"]:
            exit()
            time.sleep(0.7)
logging()
time.sleep(0.9)
print('succ sess')
# oil = input("Пожалуйста, введите выбор, который вы хотите сделать:"
#      "\n1)Откройте счет\n2)Aвторизация\n3)Выход;")
# z = ("Откройте счет")
def auth_exit():
    abb = ""
    print("Aвторизация, key ""s")
    print("Выход, key ""f""'")
    name = input('chose your option pls  ')
    #if name == 's':
    #    name = input('your name is  ')
    #    print(name)
    #if name == 'f':
    #    exit()
    #elif key != "s, f":
    #    pass
    #if name == 'cristy':
    #    print("try again please")
    if name == 'f':
        exit()
    if name == 's':
    #    name = input('input your PIN ')
        pin = input("Пожалуйста, введите номер вашей карты:")
        if pin in dictionary:
            x = dictionary1.get('pin')
            if pin == dictionary1['pin']:
                time.sleep(2)
                print('correct')
            for i in range(1):
                oil = input("Пожалуйста, введите свой пароль:")
            if oil == dictionary1['passw']:
                time.sleep(1.7)
                print('Успешный вход!')
    #            if dictionary[name]['status'] == 1:
    #                print('Пользователь был заморожен, пожалуйста, найдите сотрудника для размораживания!')
    #            exit(0)
            elif name != 's, f':
                time.sleep(1)
                input('wrong option, press enter to return')
                return(auth_exit())
                time.sleep(0.7)
auth_exit()
abc = input('1.add money\n2.give money\n ')
abc = input("select operation: + - * ")
x = dictionary1.get('money')
if abc == '+':
    print('warning you cant add more than your balance')
    time.sleep(1.1)
    x = dictionary1.get('money')
    money = int(input("how much to add?> "))
    if money >= dictionary1['money']:
        print('you cant add more than your balance, exiting...')
        time.sleep(0.6)
        exit()
    elif money < dictionary1['money']:
        time.sleep(1.3)
        print(dictionary1['money']),print('your current money')
        time.sleep(1)
        dictionary1['money'] = dictionary1['money'] + money
        time.sleep(1.6)
        print('succesefuly gived')

balance = input('wanna view you balance?')
if balance =='yes':
                time.sleep(1.4)
                print(dictionary1['money'])
elif balance == 'no':
                exit()
if abc == "-":
        print('warning you cant give more than your balance')
        time.sleep(1)
        x = dictionary1.get('money')
        money = int(input("how much to give?> "))
        if money > dictionary1['money']:
            print('you cant give more than your balance, exiting...')
            time.sleep(0.6)
            exit()
        elif money <= dictionary1['money']:
            print('well, you can give =D')
            time.sleep(0.9)
            print(dictionary1['money']),print('your current money')
            dictionary1["money"] = dictionary1["money"] - money
            time.sleep(1)
            print('succesefuly gived')
'''cache = input('wanna view you balance???')
if cache =='yes':
  time.sleep(1.4)
  print(dictionary1['money'])
elif cache == 'no':
exit()
'''
'''if abc == "*":
    money = int(input("how much to share?>"))
    if client[0]["money"] >= money:
        client[0]["money"] = client[0]["money"] - money
        client[1]["money"] = client[1]["money"] + money
    else:
        abcdee = input('press 6 to vew your currect balance')
    if abcdee == "6":
        print('a')
    elif abcdee != '6':
            exit()
'''



#print(name + 'Счет успешно открыт!')
#def fun2(password):
#    if PIN != 2001:
 #    abc = input('press enter to return')


#    return
#def fun1(qwerty):
 #   pass






























































# if oil != "D":
#    print("oo")
