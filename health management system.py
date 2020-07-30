import datetime
def gettime():
    return datetime.datetime.now()
def takevalues(k):
    if k == 1:
        c = int(input("enter 1 for exercise and 2 for food \n"))
        if (c==1):
            value = input("print the value\n")
            with open("harryexer.txt","a") as f1:
                f1.write(str([str(gettime())])+": "+value+"\n")
            print("sucessfully written")
        if c ==2:
            value = input("print the value\n")
            with open("harryfood.txt", "a") as f1:
                f1.write(str([str(gettime())]) + ": " + value + "\n")
            print("sucessfully written")
    elif k ==2:
        c = int(input("enter 1 for exercise and 2 for food \n"))
        if c == 1:
            value = input("print the value\n")
            with open("rohanexer.txt", "a") as f2:
                f2.write(str([str(gettime())]) + ": " + value + "\n")
            print("sucessfully written")
        if c == 2:
            value = input("print the value\n")
            with open("rohanfood.txt", "a") as f2:
                f2.write(str([str(gettime())]) + ": " + value + "\n")
            print("sucessfully written")
    elif k ==3:
        c = int(input("enter 1 for exercise and 2 for food \n"))
        if c == 1:
            value = input("print the value\n")
            with open("hammadexer.txt", "a") as f3:
                f3.write(str([str(gettime())]) + ": " + value + "\n")
            print("sucessfully written")
        if c == 2:
            value = input("print the value\n")
            with open("hammadfood.txt", "a") as f3:
                f3.write(str([str(gettime())]) + ": " + value + "\n")
            print("sucessfully written")
    else: print("enter valid entries")
def retvalues(k):
    if k == 1:
        c = int(input("enter 1 for exercise and 2 for food \n"))
        if c == 1:
            with open ("harryexer.txt") as f1:
                for i in f1:
                    print(i,end = " ")
        elif c ==2:
            with open ("harryfood.txt") as f1:
                for i in f1:
                    print(i,end = " ")
    elif k ==2:
        c = int(input("enter 1 for exercise and 2 for food \n"))
        if c == 1:
            with open("rohanexer.txt") as f2:
                for i in f2:
                    print(i, end=" ")
        elif c == 2:
            with open("rohanfood.txt") as f2:
                for i in f2:
                    print(i, end=" ")
    elif k == 3:
            c = int(input("enter 1 for exercise and 2 for food \n"))
            if c == 1:
                with open("hammadexer.txt") as f3:
                    for i in f3:
                        print(i, end=" ")
            elif c == 2:
                with open("hammadfood.txt") as f3:
                    for i in f3:
                        print(i, end=" ")
    else: print("enter correct values")
print("health management system: ")
a=int(input("press 1 for lock the value and 2 for retrieve "))

if a==1:
    b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
    takevalues(b)
else:
    b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
    retvalues(b)


1

