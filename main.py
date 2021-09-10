'''
Python Guessing Game

Task: Pick a number in a certain range. Make sure the player knows what that range is.
The user guesses the number. If they guess right, they win. Otherwise, have them try again.
After a number of guess, the player loses. Alternatively, implement a simple scoring algorithm.
Because of the simplicity of this game, you could implement a hint.

'''

import random
import math

#Create and store the random number
randomNumber = random.randint(1,100)

#Keep track of guesses
guessCount = 0

#Max guesses is 5
maxGuesses = 5

#Player's guess
guess = 0

#Players past guesses
guessList = []


#Main functionality of the game
while guessCount < maxGuesses:
    guess = int(input("Enter a guess between 1 - 99: "))
    if (math.isnan(guess)):
        print("Please enter a valid number.")
        print("You have " + str(maxGuesses - guessCount) + " guesses left")
    elif (guess < 1 or guess > 99):
        print("Outside of bounds. Please guess between 1-99.")
        print("You have " + str(maxGuesses - guessCount) + " guesses left")
    elif (guess in guessList):
        print("You have already guessed this number.")
        print("You have " + str(maxGuesses - guessCount) + " guesses left")
    elif (guess == randomNumber):
        guessCount += 1
        print( "Congratulations, you guessed the number " + randomNumber + " in " + guessCount + " guesses.")
    elif (guess < randomNumber):
        guessCount += 1
        guessList.append(guess)
        print("Incorrect...Guess higher!")
        print("You have " + str(maxGuesses - guessCount) + " guesses left")
    elif (guess > randomNumber):
        guessCount += 1
        guessList.append(guess)
        print("Incorrect...Guess lower!")
        print("You have " + str(maxGuesses - guessCount) + " guesses left")
print("Game over. You ran out of guesses! ")
print("The number was " + str(randomNumber))


