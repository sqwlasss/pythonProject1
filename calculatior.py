a = int(input("1-4islo:"))
b = int(input("2-4islo:"))
buter = input("select operation: + / - =")

if buter == "+":
    print(a+b)
elif buter == "*":
    print(a*b)
elif buter == "%":
    print(a%b)
else:
    print(a-b)
