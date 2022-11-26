# # print('Hello world!')
# # a = 1
# # b = 5
# # c = 'hello'
# # # d = None
# # # print(f"{c} i am {a}{b}")
# # print(c + ' i am ' + str(a) + str(b))
#
# mylist = ['banana']
# mylist.append('cherry')
# mylist.append('mango')
#
# mylist1 = ['banana']
# mylist1.append('cherry')
# mylist1.append('mango')
#
# mylist2 = mylist1 + mylist
# # # print(mylist2)
# for l in mylist2:
#     print(l[0])
#
# #
# # for l in range(6):
# #     print(mylist2[l])

thisdict = {
    'firstname': 'scebec',
    'lastname': 'cristy'
}
thisdict1 = {
    'firstname': 'scebec',
    'lastname': 'mike'
}
thisdict2 = {
    'firstname': 'scebec',
    'lastname': 'dorel'
}

list = []
list.append(thisdict)
list.append(thisdict1)
list.append(thisdict2)

for l in list:
    l['firstname'] = 'nekrasov'
    print(l)