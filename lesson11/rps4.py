import sys
import random
from enum import Enum

game_count = 0

def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCICCORS = 3

    playerchoice = input("\nEnter ... \n1 for Rock \n2 for Paper \n3 for Scissors\n\n")
    
    if playerchoice not in ["1", "2", "3"]:
        print("You need 1, 2, 3")
        return play_rps()
    else:
        playerchoice = int(playerchoice)

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(playerchoice)).replace('RPS.', ''))
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + "\n")

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return("You wins")
        elif player == 2 and computer == 1:
            return("You wins")
        elif player == 3 and computer == 2:
            return("You wins")
        elif player == computer:
            return("Tie game")
        else:
            return("Python wins")

    print(decide_winner(playerchoice, computer))


    global game_count 
    game_count += 1
    print("\nGame count : " + str(game_count))

    print("Play again?")

    while True:
        playagain = input("\nPlay again?\nY for Yes \nQ ti Quit\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("Thank you for playing!\n")
        sys.exit("Bye!")

play_rps()