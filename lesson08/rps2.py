import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCICCORS = 3

playagain = True
while playagain != False:
    playerchoice = input("\nEnter ... \n1 for Rock \n2 for Paper \n3 for Scissors\n\n")
    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("Use 1,2,3")

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', ''))
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + "\n")


    if player == 1 and computer == 3:
        print("You wins")
    elif player == 2 and computer == 1:
        print("You wins")
    elif player == 3 and computer == 2:
        print("You wins")
    elif player == computer:
        print("Tie game")
    else:
        print("Python wins")
    playagain = input("\nPlay again?\nY for Yes \nQ ti Quit\n")

    if playagain.lower() != "q":
        print("Cool! Lets Play again\n")
        continue
    else:
        print("\nFinish\nThank you for playing\n")
        playagain = False
    sys.exit("Bye!")