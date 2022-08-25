import random

player = input('write your name: ')
player_choice = input(' %s: choose paper, rock or scissors: '% player)
possible_actions = ["rock", "paper", "scissors"]
bot_action = random.choice(possible_actions)

if player_choice == bot_action:
    print("It's a tie!")
elif player_choice == "rock":
    if bot_action == "scissors":
        print("You win!")
    else:
        print("You lose.")
elif player_choice == "paper":
    if bot_action == "rock":
        print("You win!")
    else:
        print("You lose.")
elif player_choice == "scissors":
    if bot_action == "paper":
        print("You win!")
    else:
        print("You lose.")