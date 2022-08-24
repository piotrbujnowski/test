import random
player = input('write your name: ')
playerchoice = input(' %s: choose paper, rock or scissors: '% player)

choices = ["paper","rock","scissors"]
botchoice = random.choice(choices)

if int(playerchoice) == 'paper' and int(botchoice) == 'rock':
    print('you win!')
elif int(playerchoice) == 'paper' and int(botchoice) == 'scissors':
    print('you loose!')