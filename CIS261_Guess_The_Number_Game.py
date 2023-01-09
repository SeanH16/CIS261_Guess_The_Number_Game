#create a function to display heading
#Create loop to play game again

#Sean Holbrook
#CIS261
#Guess The Number Game


import random

guess = 0
guessesTaken = 0
user_limit = input("Please input a top limit number for a guessing game: ")
user_limit = int(user_limit)

secretNumber = random.randint(1, user_limit)
print(f'I am thinking of a number between 1 and {user_limit}.')

#Ask the player to guess.
while secretNumber != guess:
    print('Take a guess.')
    guess = int(input())
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
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

