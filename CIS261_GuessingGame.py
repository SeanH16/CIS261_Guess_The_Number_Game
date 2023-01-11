#Sean Holbrook
#CIS261
#Guess The Number Game

import random

def display():
    print("Guess the number game!")
    print()

display()

guess = 0
guessesTaken = 0
user_limit = input("Please input a top limit number for a guessing game(1 - ?): ")
user_limit = int(user_limit)

secretNumber = random.randint(1, user_limit)
print(f'I am thinking of a number between 1 and {user_limit}.')
print('Take a guess.')

#Ask the player to guess.
def number_game(secretNumber, guess, guessesTaken):
    while secretNumber != guess:
        guess = int(input())
        #fix this so it resets on new_game
        guessesTaken += 1

        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            break #this condition is the correct guess
        
    if guess == secretNumber:
        print('Good job! You guessed my number in ' + str(guessesTaken) +
            ' guesses!')
        new_game = input("Do you want to play again? (y/n): ")
        if new_game.lower() == "y":
            #need to clean this up into a function
            user_limit = input("Please input a top limit number for a guessing game(1 - ?): ")
            user_limit = int(user_limit)
            secretNumber = random.randint(1, user_limit)
            print(f'I am thinking of a number between 1 and {user_limit}.')
            print('Take a guess.')
            number_game(secretNumber, guess, guessesTaken)
        else:
            print("Goodbye!")
            

number_game(secretNumber, guess, guessesTaken)