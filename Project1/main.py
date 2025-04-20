# Project 1
# We all have played snake, water gun game in our childhood. If you haven’t, google the
# rules of this game and write a python program capable of playing this game with the
# user.

# The game is played between two players. Each player chooses one of three options: snake, water, or gun.
# The winner is determined by the following rules:
# - Snake beats water (snake drinks water)
# - Water beats gun (water washes gun)
# - Gun beats snake (gun shoots snake)
# - If both players choose the same option, it's a tie.
# - The game continues until one player wins a predetermined number of rounds (e.g., 3 rounds).
# - The program should keep track of the score and display it after each round.

import random

choices = [1, 0, -1]

computer = random.choice(choices)

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

print("Choose an option as mentioned below: ")
print("s for Snake, w for Water, g for Gun")
your_choice = input("Enter your choice: ")
you = youDict[your_choice]

# By now we have 2 numbers (variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if (computer == you):
    print("Its a draw!")

else:
    if (computer == -1 and you == 1):
        print("You win!")

    elif (computer == -1 and you == 0):
        print("You Lose!")

    elif (computer == 1 and you == -1):
        print("You lose!")

    elif (computer == 1 and you == 0):
        print("You Win!")

    elif (computer == 0 and you == -1):
        print("You Win!")

    elif (computer == 0 and you == 1):
        print("You Lose!")

    else:
        print("Something went wrong!")
