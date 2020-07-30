import random
name = input("enter your name:")
a = 10 #total chance
n = 0  #no of games
np = 0 #no of game won by player
nc = 0 #no of game won by comp
l = ["snake","water","gun"]
while n < a:
    choose = input("enter your choice\n snake\n water\n gun\n ")
    comp = random.choice(l)
    if choose == "snake":
        if comp == choose:
            print(f"match is draw {choose} vs {comp}")
        elif comp == "water":
            print(f"you won {choose} vs {comp}")
            np+=1
        elif comp == "gun":
            print(f"you loose {choose} vs {comp}")
            nc+=1
    elif choose == "water":
        if comp == choose:
            print(f"match is draw {choose} vs {comp}")
        elif comp == "snake":
            print(f"you loose {choose} vs {comp}")
            nc+=1
        elif comp == "gun":
            print(f"you win {choose} vs {comp}")
            np+=1
    elif comp == "gun":
        if comp == choose:
            print(f"match is draw {choose} vs {comp}")
        elif comp == "water":
            print(f"you loose {choose} vs {comp}")
            nc+=1
        elif comp == "snake":
            print(f"you win {choose} vs {comp}")
            np+=1
    else:
        print(f"you entered wrong choice")
    n+=1
    print(f"{a - n} is left out of {a} \n")
if(np > nc):
    print(f" {name} won")
else:
    print(f" {name} loose")