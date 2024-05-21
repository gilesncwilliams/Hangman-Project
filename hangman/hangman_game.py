"""The classic game of hangman.

The computer selects a word at random for a user to guess.
"""


import random


class Hangman:
    """Sets up a game of hangman.

    Attributes:
        word_list (list): a list of words that the computer can choose from at random.
        num_lives (int): the number of lives the user starts with.
    """
    def __init__(self, word_list, num_lives=5):
        """Intialises the instance of the game.
        
        Args:
          word (string): a word chosen at random by the computer.
          word_guessed (list): a list containing each letter of the word the user has to guess.
          num_letters (int): the number of unique letters in the word.
          list_of_guesses (list): a list of the letters the user has already guessed.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = int(len(set(self.word)))
        self.list_of_guesses = []

    def check_guess(self, guess):
        """Checks each guess to see if it is in the word.  

        Attributes:
          guess (string): a single letter guess. 
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! \"{guess}\" is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess 
            print(self.word_guessed)              
            self.num_letters = self.num_letters - 1
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, \"{guess}\" is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left")
    
    def ask_for_input(self):
        """Validates the user's guesss.
        """
        while True: 
            guess = input("Please enter a single letter: ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    """Runs the game of hangman.
    """
    game = Hangman(word_list)
    while True:
        game.ask_for_input()
        if game.num_lives == 0:
            print("You Lost!")
            break
        elif game.num_letters == 0:
            print("Congratulations. You won the game!")
            break


if __name__ == '__main__':          
    word_list = ["apple", "blueberry", "pear", "banana", "lime"]
    play_game(word_list)

