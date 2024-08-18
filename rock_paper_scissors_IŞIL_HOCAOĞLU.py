import random

computer_score = 0
player_score = 0
round_number = 1
game_number = 1
list = ["rock", "paper", "scissors"]
continuity = ["yes", "no"]


def rock_paper_scissors_IŞIL_HOCAOĞLU():
    global computer_score, player_score, round_number, game_number

    print(
        "We are playing Rock, paper, and scissors!\nRock wins scissors\nPaper wins rock\nScissors wins paper\nWe will play 3 rounds and whoever wins a total of 2 rounds, wins the game.\nEnter rock, paper, or scissors to play, or if you do not want to play, write 'exit'. \nThe game starts now!\nGame 1, Round 1")

    while True:
        computer_choice = random.choice(list)
        player_choice = input("rock, paper, scissors, or exit? : ")

        if player_choice == "exit":
            print("Thanks for playing! Goodbye!")
            break

        if player_choice not in list:
            print("Invalid choice, please choose rock, paper,scissors or exit.")
            continue

        print(f"Computer chose: {computer_choice}")

        if computer_choice == player_choice:
            round_number += 1
            print("It's a tie this round!")
            print("######################")
        elif (computer_choice == "rock" and player_choice == "scissors") or \
                (computer_choice == "scissors" and player_choice == "paper") or \
                (computer_choice == "paper" and player_choice == "rock"):
            round_number += 1
            print("You lost this round!")
            print("####################")
            computer_score += 1
        else:
            round_number += 1
            print("You won this round!")
            print("###################")
            player_score += 1

        if computer_score < 2 and player_score < 2:
            print(f"Player: {player_score}, Computer: {computer_score}")
            print(f"Game {game_number}, Round {round_number}")

        if computer_score == 2 or player_score == 2:
            if player_score > computer_score:
                print("Congratulations! You won the game!")
            else:
                print("The computer won the game!")

            player = input("Do you want to challenge me again? (yes/no):")
            computer = random.choice(continuity)
            if player == "yes" and computer == "yes":
                print("I want to play again as well! Let's play one more!")
                computer_score = 0
                player_score = 0
                round_number = 1
                game_number += 1
                print(f"Starting Game {game_number}!")
                print(f"Game {game_number}, Round {round_number}")
            elif player not in continuity:
                print("Invalid choice, please yes or no:")
            elif player == "no":
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("Computer doesn't want to play.")
                break


print(rock_paper_scissors_IŞIL_HOCAOĞLU())

