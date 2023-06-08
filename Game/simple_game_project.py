import random

def gamewin(computer,you):
    if computer==you:
        return None

    elif computer=='s':
        if you=='p':
            return False
        elif you=='c':
            return True

    elif computer=='p':
        if you=='s':
            return True
        elif you=='c':
            return False

    elif computer=='c':
        if you=='s':
            return False
        elif you=='p':
            return True

print("Computer's Turn:Choose from Stone(s) Paper(p) Scissors(c):")
randomNo=random.randint(1,3)
if randomNo==1:
         computer='s'

elif randomNo==2:
         computer='p'

elif randomNo==3:
         computer='c'

you=input("Your Turn:Choose from Stone(s) Paper(p) Scissors(c):")

winner=gamewin(computer,you)

print("Computer chose:",computer)
print("You chose:",you)

if winner==None:
    print("Game is Tied!")

elif winner:
    print("Computer Wins!")

else:
    print("You Wins!")


