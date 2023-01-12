#Sean Holbrook
#CIS261
#Guess The Number Game

import random

#display function for game title
def display():
    print("Guess the number game!")
    print()

display()

#Variable initialization and user limit
guess = 0
user_limit = input("Please input a top limit number for a guessing game(1 - ?): ")
user_limit = int(user_limit)

#Variable initialization using random and print
secret_number = random.randint(1, user_limit)
print(f'I am thinking of a number between 1 and {user_limit}.')
print('Take a guess.')


#Ask the player to guess main function
def number_game(secret_number, guess):
    guesses_taken = 0
    while secret_number != guess:
        guess = int(input())
        guesses_taken += 1

        if guess < secret_number:
            print('Your guess is too low.')
        elif guess > secret_number:
            print('Your guess is too high.')
        else:
            break #this condition is the correct guess
        
    if guess == secret_number:
        print(f'Good job! You guessed my number in {guesses_taken} guesses!')
        new_game = input("Do you want to play again? (y/n): ")
        if new_game.lower() == "y":
            #need to clean this up into a function
            user_limit = input("Please input a top limit number for a guessing game(1 - ?): ")
            user_limit = int(user_limit)
            secret_number = random.randint(1, user_limit)
            print(f'I am thinking of a number between 1 and {user_limit}.')
            print('Take a guess.')
            number_game(secret_number, guess)
        else:
            print("Goodbye!")
            
#Start the main game function
number_game(secret_number, guess)
