import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = int(len(set(self.word)))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! \"{guess}\" is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess 
            #print statement to check the letter was added to the 'word_guessed' list
            print(self.word_guessed)              
            self.num_letters = self.num_letters - 1
            #print statement to check 'num_letters' was reduced by 1
            print(self.num_letters)     
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, \"{guess}\" is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left")
    
    def ask_for_input(self):
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
    game = Hangman(word_list)
    while True:
        game.ask_for_input()
        if game.num_lives == 0:
            print("You Lost!")
            break
        elif game.num_letters == 0:
            print("Congratulations. You won the game!")
            break

        
word_list = ["apple", "blueberry", "pear", "banana", "lime"]
play_game(word_list)

