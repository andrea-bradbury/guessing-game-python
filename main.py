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

        # Initialise visual components base
        EasyFrame.__init__(self, title="Guessing Game", width=500, height=100, resizable=False)

        # Add game communication display (label)
        self.guessLabel = self.addLabel(text="Guess: ", row=0, column=0)
        # Add user input area (input field)
        self.guessField = self.addIntegerField(value=0, row=0, column=1)

        # Add final result display (label)
        self.resultLabel = self.addLabel(text="", row=1, column=0, background="White")

        # Add remaining guesses display (label)
        self.guessesLeftLabel = self.addLabel(text="Guesses: ", row=2, column=0, sticky="W")
        # Add user input confirmation (button)
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
        """
        Updates the remaining guess count
        """
        self.guessesLeftLabel["text"] = f"Guesses: {self.maxGuesses - self.guessCount}"

    def ValidNumber(self, value):
        """
        Tests a provided number, sets self.guess to it if valid
        :param value: String: The provided number to test
        :return: Bool: If it was successful
        """
        try:
            # try to parse the number
            test = int(value)
        except ValueError:
            # return false if unsuccessful
            return False
        # is successful set guess to output
        self.guess = test
        # return true if successful
        return True

    def TryInput(self):
        """
        Goes trough all error catching, trying each, before returning true if passed all or false if failed one
        :return: Bool: if the code passed all user error handling
        """
        # If the user has passed the max number of allowed guesses
        if self.guessCount >= self.maxGuesses:
            # do not pass go, do not collect $200
            return False

        # Test if user number is valid
        if not self.ValidNumber(self.guess):
            self.resultLabel["text"] = "Please enter a valid number."
            return False

        # Test if user number is within the allowed input range
        if self.guess < 1 or self.guess > 99:
            self.resultLabel["text"] = "Outside of bounds. Please enter a guess between 1 - 99."
            return False

        # Test if user has already guessed the number
        if self.guess in self.guessList:
            self.resultLabel["text"] = "You have already guessed this number."
            return False

        return True

    def MakeGuess(self):
        # Get the user entered number
        self.guess = self.guessField.getValue()

        # if the input is valid to TryInput's filters
        if self.TryInput():
            # If the number matches the generated number
            if self.guess == self.randomNumber:
                self.resultLabel["text"] = f"Congratulations, you guessed the number in {self.guessCount} guesses!"

            # If the guess is less than the generated number
            elif self.guess < self.randomNumber:
                self.guessList.append(self.guess)
                self.resultLabel["text"] = "Incorrect, guess higher!"

            # If the guess is more than the generated number
            elif self.guess > self.randomNumber:
                self.guessList.append(self.guess)
                self.resultLabel["text"] = "Incorrect, guess lower!"

            # add a move and update game state
            self.guessCount += 1
            self.UpdateGame()

            # If the game is now over/equal to max moves, game over
            if self.guessCount >= self.maxGuesses:
                self.resultLabel["text"] = f"Game over, you ran out of guesses!\nThe number was: {self.randomNumber}"


game = GuessingGame()

game.mainloop()


