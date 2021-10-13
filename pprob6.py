#Guess the number
import random

Play = "Y"
while Play == "Y":
    Guess = 999
    counter = 0
    Number = round(random.random() * 100)

    #print(Number)
    
    while Guess != Number:
        counter += 1
        Guess = int(input("Guess a number between 1-100 "))

        if Guess > Number:
           print("Too high. Try a lower number. ")
        if Guess < Number:
           print("Too low. Try a higher number. ")

    print("It took" ,counter, "tries to guess" ,Number,".")
    print()

    Play = (input("Do you want to play again? Y or N "))
