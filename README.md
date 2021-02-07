# rock-paper-scissors-inclass

A Python application for students to run a "rock, paper, scissors" simulation game against the computer. 


## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository] (https://github.com/mjh2323/rock-paper-scissors-inclass) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```
cd ~/Desktop/rock-paper-scissors-exercise
```

Use your text editor or the command-line to create a file in that repo called "game.py", and then place the following contents inside:

```
# game.py
print("Rock, Paper, Scissors, Shoot!")
```
Create and activate a new project-specific Anaconda virtual environment:

```
conda create -n my-game-env python=3.8 # (first time only)
conda activate my-game-env

```


From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

```
python game.py
```

__________________________________________________________________________
Now you can begin the implementation portion of the exercise 
# 
#
Paste the following code in your "game.py" file: 


`````````````````````````````
# game.py

import random

player_name = input("Hello and welcome, please enter your name: ")
print("Rock, Paper, Scissors, Shoot!")



print("-------------------")
print("Welcome", player_name, "to my Rock-Paper-Scissors game...")
print("-------------------")




user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

print(user_choice)
print("You chose:", user_choice)




# simulating a computer input 

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

print("The computer chose:", computer_choice)


#
# validate user selection 
#
# stop the program and not try to determine the winner)
# if the user choice is invalid

#
# determining who won 
#

if user_choice == computer_choice:
    print("It's a tie!")

if user_choice == "rock":
    if computer_choice == "rock":
        print("Maybe next time.")
    elif computer_choice == "paper":
        print("Oh, the computer won. It's ok.")
    elif computer_choice == "scissors":
        print("Oh, you won! Nice job.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Oh, you won! Nice job.")
    elif computer_choice == "paper":
        print("Maybe next time.")
    elif computer_choice == "scissors":
        print("Oh, the computer won. It's ok.")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("Oh, the computer won. It's ok.")
    elif computer_choice == "paper":
        print("Oh, you won! Nice job.")
    elif computer_choice == "scissors":
        print("Maybe next time.")
else:
    print("It seems you entered incorrectly! Please only enter either rock, paper, or scissors next time.")



exit()

````````````````````````````````

#

#

_______________________________________________

An understanding of the functions used: 

1) "input()" - the "input()" function is used to allow the user to enter their own name, as well as their choice when playing the game. 

2) "import random" - this is used at the beginning of the file to allow the computer to randomly generate either "rock", "paper", or "scissors" when the game is running

3) "player_name", "user_choice", "computer_choice" - these variables hold the inputs and then can be referenced throughout the code, so that the user does not have to repeatedly enter the information manually. 

4) the if funciton - the "if" function tells the program to print a statement based on the computer and user choices. For example, "if" the computer picks scissors and the user picks scissors, "then" the program will print "its a tie" 

5) exit() - will be used to end the program 

