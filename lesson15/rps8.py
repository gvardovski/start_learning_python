import sys
import random

from enum import Enum

def rps(name=""):
    game_count = 0
    player_wins = 0
    pc_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal pc_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCICCORS = 3

        playerchoice = input(f"\n{name}, please enter ... \n1 for Rock \n2 for Paper \n3 for Scissors\n\n")
        
        if playerchoice not in ["1", "2", "3"]:
            print(f"{name} please enter 1, 2, 3")
            return play_rps()
        else:
            playerchoice = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(f"\n{name} you chose {str(RPS(playerchoice)).replace('RPS.', '').title()}")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()} \n")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal pc_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return(f"{name}, you win")
            elif player == 2 and computer == 1:
                player_wins += 1
                return(f"{name}, you win")
            elif player == 3 and computer == 2:
                player_wins += 1
                return(f"{name}, you win")
            elif player == computer:
                return("Tie game")
            else:
                pc_wins += 1
                return f"Python wins! Sorry {name}!"

        print(decide_winner(playerchoice, computer))

        nonlocal game_count 
        game_count += 1
        print(f"\nGame count : {game_count}")
        print(f"{name}'s wins  : {player_wins}")
        print(f"PC wins  : {pc_wins}")

        while True:
            playagain = input(f"\nPlay again, {name}?\nY for Yes \nQ ti Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print(f"Thank you for playing {name}!\n")
            sys.exit("Bye!")
    return play_rps


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalize game experience")
    parser.add_argument("-n", "--name", metavar="name",
                        required=True, help="The name of the person playing the game")
    args = parser.parse_args()

    play_only_in_main = rps(args.name)
    play_only_in_main()