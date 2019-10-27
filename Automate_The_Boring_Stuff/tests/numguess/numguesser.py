#!/usr/bin/env python
# numguesser.py

# Import modules
import random

# Variable Declaration
intComputerGuess = 0
intHumanGuess = 0

# Randomly assign an int to intComputerGuess
intComputerGuess = random.randint(1,10)

# Get initial human guess
intHumanGuess = int(input())

while True:
    if intComputerGuess == intHumanGuess:
        print("Yay you did it!")
        break
    else:
        print("Sorry didn't workout, try again. Would you like to buy one our loot boxes to help you get through this level? Just 2 gems!")
        intHumanGuess = int(input())