
list = []
book1 = {'name':'Harry Potter 1', 'content':'qwedsdcsdf text blabla'}
book2 = {'name':'Harry Potter 2', 'content':'some text blabla'}
book3 = {'name':'Harry Potter 3', 'content':'somesdfasdfasdfa'}
book4 = {'name':'50 shades of pink', 'content':'sosdfxt blabla'}
book5 = {'name':'book5', 'content':'keksosdfxt blabla'}
book7 = {'name':'book7', 'content':'some asdtext blabla'}
book6 = {'name':'book6', 'content':'some t1111ext blabla'}

list.append(book1)
list.append(book2)
list.append(book3)
list.append(book4)
list.append(book5)
list.append(book6)
list.append(book7)

b = 'Harry Potter'
# for l in list:
#     print(l['name'])

for l in list:
    if b in l['name']:
        print(l)