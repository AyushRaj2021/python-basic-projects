def fibonakkki(n):
    if n == 1:
         return 0
    elif n==2:
        return 1
    else:
       return fibonakkki(n-1) + fibonakkki(n-2)
num= int(input("enter the no:"))
print(fibonakkki(num))
