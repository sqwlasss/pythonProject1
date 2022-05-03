dictionary = {
    "02001":{
   'name1' : 'cristy',
   'passw' : '0808',
   'money' : 777,
   "status": 0
}
}
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
            if dictionary[name]['status'] == 1:
                print('Пользователь был заморожен, пожалуйста, найдите сотрудника для размораживания!')
    #print(name + 'Счет успешно открыт!')
#def fun2(password):
#    if PIN != 2001:
 #    abc = input('press enter to return')


#    return
#def fun1(qwerty):
 #   pass






























































# if oil != "D":
#    print("oo")
