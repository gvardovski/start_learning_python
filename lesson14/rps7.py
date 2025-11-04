import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    pc_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal pc_wins

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

        print(f"\nYou chose {str(RPS(playerchoice)).replace('RPS.', '').title()}")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()} \n")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal pc_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return("You wins")
            elif player == 2 and computer == 1:
                player_wins += 1
                return("You wins")
            elif player == 3 and computer == 2:
                player_wins += 1
                return("You wins")
            elif player == computer:
                return("Tie game")
            else:
                pc_wins += 1
                return("Python wins")

        print(decide_winner(playerchoice, computer))

        nonlocal game_count 
        game_count += 1
        print(f"\nGame count : {str(game_count)}")
        print(f"Player wins  : {str(player_wins)}")
        print(f"PC wins  : {str(pc_wins)}")

        print("\nPlay again?")

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
    return play_rps

play_only_in_main = rps()

if __name__ == "__main__":
    play_only_in_main()