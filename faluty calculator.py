a = int(input("enter the no a: "))
b = int(input("enter the no b: "))
print('what you want to do : + ,- * /')
opd = str(input())
if a == 45 and b == 3 and opd == '*':
    print('555')
elif a == 56 and b == 9 and opd == '+':
    print('77')
elif a == 56 and b == 6 and opd == '/':
    print('4')
elif opd == '+':
    out = a+b
    print(out)
elif opd == '-':
    out = a-b
    print(out)
elif opd == '*':
    out = a*b
    print(out)
else:
    out = a/b
    print(out)
