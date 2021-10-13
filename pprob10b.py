#Rock Paper Scissors
#Katie King

import random

ucounter = 0
ccounter = 0

for i in range (5):
    user = input("Choose Rock, Paper, Scissors, Spock, Lizard (R, P, S, Sp, L) ")
    number = (int(random.randint(1,5)))

    print(number)

    if number == 1:
        computer = ("R")
    elif number == 2:
        computer =("P")
    elif number == 3:
        computer = ("S")
    elif number == 4:
        computer = ("Sp")
    elif number == 5:
        computer = ("L")

    print("Computer chooses ",computer)

    if user == computer:
        print("Tie Game")
        print("Computer = ",ccounter,".\n Player = ",ucounter,".")
    if user =="R" and computer == "S"  or user == "R" and computer == "L" or user == "P" and computer == "R" or user == "P" and computer == "Sp" or user == "S" and computer == "P" or user == "S" and computer == "L"or user == "Sp" and computer == "S" or user == "Sp" and computer == "R" or user == "L" and computer == "Sp" or user == "L" and user == "P":
        print("You win!")
        ucounter += 1
        print("Computer = ",ccounter,".\n Player = ",ucounter,".")
    if computer =="R" and user == "S"  or computer == "R" and user == "L" or computer == "P" and user == "R" or computer == "P" and user == "Sp" or computer == "S" and user == "P" or computer == "S" and user == "L"or computer == "Sp" and user == "S" or computer == "Sp" and user == "R" or computer == "L" and user == "Sp" or computer == "L" and user == "P":
        print("I win")
        ccounter += 1
        print("Computer = ",ccounter,".\n Player = ",ucounter,".")

if ucounter > ccounter:
    print()
    print("You win")
    print("Computer = ",ccounter,".\n Player = ",ucounter,".")
elif ucounter < ccounter:
    print()
    print("I win")
    print("Computer = ",ccounter,".\n Player = ",ucounter,".")
else:
    print()
    print("Tie game")
    print("Computer = ",ccounter,".\n Player = ",ucounter,".")
