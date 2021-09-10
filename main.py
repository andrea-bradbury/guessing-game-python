'''
Python Guessing Game

Task: Pick a number in a certain range. Make sure the player knows what that range is.
The user guesses the number. If they guess right, they win. Otherwise, have them try again.
After a number of guess, the player loses. Alternatively, implement a simple scoring algorithm.
Because of the simplicity of this game, you could implement a hint.

'''

import random
import math
from breezypythongui import EasyFrame

class GuessingGame(EasyFrame):

    def __init__(self):

        EasyFrame.__init__(self, title="Guessing Game", width=500, height=100, resizable=False)

        self.guessLabel = self.addLabel(text="Guess: ", row=0, column=0)
        self.guessField = self.addIntegerField(value=0, row=0, column=1)

        self.resultLabel = self.addLabel(text="", row=1, column=0, background="White")

        self.guessesLeftLabel = self.addLabel(text="Guesses: ", row=2, column=0, sticky="W")
        self.addButton(text="Guess!", row=2, column=1, command=self.MakeGuess)

        # Create and store the random number
        self.randomNumber = random.randint(1, 100)

        # Keep track of guesses
        self.guessCount = 0

        # Max guesses is 5
        self.maxGuesses = 5

        # Player's guess
        self.guess = 0

        # Player's past guesses
        self.guessList = []

        # Displays default guesses
        self.guessesLeftLabel["text"] = f"Guesses: {self.maxGuesses}"

    def UpdateGame(self):
        self.guessesLeftLabel["text"] = f"Guesses: {self.maxGuesses - self.guessCount}"

    def MakeGuess(self):
        self.guess = self.guessField.getNumber()

        if self.guessCount >= self.maxGuesses:
            return

        if math.isnan(self.guess):
            self.resultLabel["text"] = "Please enter a valid number."
        elif self.guess < 1 or self.guess > 99:
            self.resultLabel["text"] = "Outside of bounds. Please enter a guess between 1 - 99."
        elif self.guess in self.guessList:
            self.resultLabel["text"] = "You have already guessed this number."
        elif self.guess == self.randomNumber:
            self.guessCount += 1
            self.resultLabel["text"] = f"Congratulations, you guessed the number in {self.guessCount} guesses!"
            self.UpdateGame()
        elif self.guess < self.randomNumber:
            self.guessCount += 1
            self.guessList.append(self.guess)
            self.resultLabel["text"] = "Incorrect, guess higher!"
            self.UpdateGame()
        elif self.guess > self.randomNumber:
            self.guessCount += 1
            self.guessList.append(self.guess)
            self.resultLabel["text"] = "Incorrect, guess lower!"
            self.UpdateGame()

        if self.guessCount >= self.maxGuesses:
            self.resultLabel["text"] = f"Game over, you ran out of guesses!\nThe number was: {self.randomNumber}"


game = GuessingGame()

game.mainloop()


