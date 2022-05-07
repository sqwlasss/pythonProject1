import random

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
   'money' : 777,
    'pin' : '02001'
}

client = []
#client.append('person')
person = {"name": "cristy", "money": 777, "PIN": "1"}
PIN = 2001
a = input("write your name please:")
b = input("PIN:")
# oil = input("Пожалуйста, введите выбор, который вы хотите сделать:"
#      "\n1)Откройте счет\n2)Aвторизация\n3)Выход;")
# z = ("Откройте счет")
key = ""
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
if name == 's':
#    name = input('input your PIN ')
    name = input("Пожалуйста, введите номер вашей карты:")
    if name in dictionary:
        for i in range(1):
            oil = input("Пожалуйста, введите свой пароль:")
        if oil == dictionary[name]['passw']:
            print('Успешный вход!')
#            if dictionary[name]['status'] == 1:
#                print('Пользователь был заморожен, пожалуйста, найдите сотрудника для размораживания!')
#            exit(0)
abc = input('1.add money\n2.give money\n ')
if abc == '+':
    money = int(input("how much to add?> "))
    if money == (random.randrange(1, 999)):
        print(dictionary1['money'])
        dictionary1['money'] = dictionary1['money'] + money
else:
 print('succesefuly gived')
 if abc == "-":
        money = int(input("how much to give?>"))
        dictionary["money"] = dictionary["money"] - money
if key == "*":
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




#print(name + 'Счет успешно открыт!')
#def fun2(password):
#    if PIN != 2001:
 #    abc = input('press enter to return')


#    return
#def fun1(qwerty):
 #   pass






























































# if oil != "D":
#    print("oo")
