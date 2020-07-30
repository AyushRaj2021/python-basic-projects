a = int(input("enter the value of n:"))
print("Type 1 or 0")
b = bool(int(input()))
if b == True:
    for i in range(1,a+1):
        for j in range(1,i+1):
            print("*",end = " ")
        print()
elif b == False:
#-1 is importnt for reverse counting
    for i in range(a,0,-1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()

