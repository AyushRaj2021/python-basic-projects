n = 18
i = 1
print('you can only play the game for 9  times')
while i<=9:
    a = int(input("enter the number: \n"))
    if a<18:
        print('you have guessed less number guess more\n')
    elif a >18:
        print('you have guessed more number guess less\n')
    else:
        print('you won\n')
        print('no of guesses taken',i)
        break
    print('no of guesses left',9-i)
    i = i+1
    if i> 9:
        print('game over')


