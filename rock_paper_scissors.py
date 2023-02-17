import random

def main():
    print("Hello!")
    print("How to play: Two players secretly pick one of rock, paper, or scissors. Both players reveal their selection to the other player at once; the winner is chosen based on what the selections are. Rock beats scissors (by crushing them); scissors beats paper (by cutting it); and paper beats rock (by covering it). If both players select the same one, it is a tie.")
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print("computer chose: " + computer_action)
    return 0


if __name__ == "__main__":
    main()