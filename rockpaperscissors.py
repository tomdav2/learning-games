#Author
#Tomdav
# rock paper scissors game

import random
RPS = ["rock","paper","scissors"]

player1 = random.choice(RPS)
player2 = input('rock paper or scissors\n')

print("you chose " + player2 + "\ncomp chose " + player1)
if player1 == player2:
    print("draw!")
elif player1 == "scissors" and player2 == "rock":
    print("YOU WIN!")
elif player1 == "rock" and player2 == "paper":
    print("YOU WIN!")
elif player1 == "paper" and player2 == "scissors":
    print("YOU WIN!")
else:
    print("YOU LOSE!")
