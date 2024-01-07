
# Rock paper scissors
# 23/12/2023

# 1. packages

import random as rand
import json
import os

print("Welcome to my first game: ROCK - PAPER - SCISSORS")
print("The goal is to win rock paper scissors 3 times in a row") 

# 2. starting values 

options = ['rock', 'paper', 'scissors']
play_again = True  

with open("schaar_steen_papier\scoreboard.txt", "r") as fp:
  scoreboard = json.load(fp)

# 3. functions 

def play_game(max_score = 3): 
    """ Play paper scissors rock """

    rounds = 0
    pc_score = 0
    user_score = 0

    # loop to win at least x number of times
    while pc_score < max_score and user_score < max_score: 

        user_choice = input("Tell what you want to choose: ").lower()
        pc_choice = rand.choice(options)

        # check if user input is allowed 
        if user_choice not in options: 
            print('You have to choose either rock, paper or scissors')
            continue 
        else: 
            next  

        # check who won 
        if pc_choice == user_choice: 
            print('Tie')
        elif pc_choice == 'rock' and user_choice == 'paper': 
            print('You win!')
            user_score += 1 
        elif pc_choice == 'paper' and user_choice == 'scissors': 
            print('You win!')
        elif pc_choice == 'scissors' and user_choice == 'rock': 
            print('You win!')
        else: 
            print('You lose!')
            pc_score += 1 

        rounds += 1
        print("Current score: " + str(user_score) + " - " + str(pc_score) )
        print("This was the " + str(rounds) + "th round")

    return pc_score, user_score


# 4. game 

while play_again: 

    user_name = input("First, tell me your name: \n")

    pc_score, user_score = play_game(max_score=1)

    if user_name not in scoreboard: 
        scoreboard[user_name] = 0

    if pc_score > user_score: 
        print('You lost! \nThe final score was ' + str(user_score) + " - " + str(pc_score) + '.')
    else: 
        print('You won, congratulations! \nThe finale score was ' + str(user_score) + " - " + str(pc_score) + '.')
        scoreboard[user_name] += 1

    with open("schaar_steen_papier\scoreboard.txt", "w") as fp:
        json.dump(scoreboard, fp)

    print(scoreboard)

    play_input = input('Want to play again? (answer with yes or no)\n')  

    if play_input.lower() != 'yes': 
        play_again = False
        print("Thanks for playing")
    else: play_again = True        
