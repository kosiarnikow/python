import random

def game():

    arrey = ["rock", "paper", "sissors"]
    c = input("\n what you choose? \n 1. rock | 2. paper | 3. sissors: ")

    print("you - " + arrey[int(c) - 1])
    print("coputer - " + random.choice(arrey))
    ret()

def ret():
    next = input("do you want to repeat the game? (y or n): ")
    if next == "y":
        game()
    else:
        print("OK")

game()

# kamien < papier
# kamien > nozyce
# papier < nozyce