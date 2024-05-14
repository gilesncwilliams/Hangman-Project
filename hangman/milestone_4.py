import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = int(len(set(self.word_guessed)))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! \"{guess}\" is in the word.")
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[guess] = guess
            self.num_letter = self.num_letter - 1
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, \"{guess}\" is not in the word. Try again.")
            print(f"You have{self.num_lives} lives left")
    
    def ask_for_input(self, guess):
        while True: 
            self.guess = input("Please enter a single letter:")
            if len(self.guess) == 1 and self.guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif self.guess in self.list_of_guesses:
                print("You already tried that letter!")    
            else:
                self.check_guess(self.guess)
                self.list_of_guesses.append(self.guess)



