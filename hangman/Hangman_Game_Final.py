import random

class Hangman:
    '''
    This class is used to run a game of hangman.
    
    Attributes passed as parameters to each instance of the class:
        word_list (list): a list of words that the computer can choose from at random.
        num_lives (int): the number of lives the user starts with a the beginning of the game.

    Attributes defined using other attributes:
        word (string): a word chosen at random by the computer for he user to guess.
        word_guessed (list): a list containing each letter of the word the user has to guess; each letter is set "_". 
        num_letters (int): the number of unique letters in the word the user has to guess.
        list_of_guesses (list): a list of the letters the user has already guessed, to avoid duplication.
    '''  
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = int(len(set(self.word)))
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        This method checks each valid guess the user makes to see if it is or isn't in the word they are trying to guess. It will:
        - convert the guess to lower case
        - if the guess is in the word it will print confirmation to the user and add the guessed letter to the word_guessed list. It will then reduced the number of unique letters by 1
        - if the guess is not in the word it will inform the user, remove a life from user's lives, and display the number of lives left using the num_lives attribute.

        Attributes:
        guess (string): a single letter guess. 
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! \"{guess}\" is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess 
            #print statement to show the correcly guessed letter in word they are trying to guess..as displayed in the 'word_guessed' list
            print(self.word_guessed)              
            self.num_letters = self.num_letters - 1
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, \"{guess}\" is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left")
    
    def ask_for_input(self):
        '''
        This method asks the user to guess a letter of the word chosen by the computer and checks if the guess is valid. 
        It is while loop that will repeat until the users inputs a valid guess, at which point it will call the check guess method and add the guess to the list_of_guesses list (in case the user tries to guess with that letter again), before breaking out of the loop.
        '''
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
    '''
    This function starts and plays the game.
    The function takes in the word_list as a parameter. The word list is a list of words the computer can choose from the play the game.
    The user wins by guess all the letters in the word before they lose all their lives from wrong guesses.
    '''
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

