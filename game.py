# game.py

import random

print("Rock, Paper, Scissors, Shoot!")



print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")




user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

print(user_choice)
print("You chose:  {user_choice}")




# simulating a computer input 

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

print("The computer chose: {computer_choice}")

exit()


