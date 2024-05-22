# Hangman Game Project

## Introdution
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Installation Instructions
Python3 is required to run this game.

Follow these instruction to [clone this repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository) to your local machine.


## Usage Instructions

### How to play the game

To play the game, ensure the current working directory is set to the location you cloned the hangman_project repository to. 
Then run the hangman_game.py script from you Command Line.


![Screenshot 2024-05-22 at 17 21 23](https://github.com/gilesncwilliams/hangman_project/assets/150936411/1d71f32d-4423-4362-a96e-ffb03b88d3fe)

### List of Words

You can create your own list of words for the computer to choose from. 
To do so simply replace the words in the word_list within the hangman_game.py code.


![Screenshot 2024-05-22 at 17 11 26](https://github.com/gilesncwilliams/hangman_project/assets/150936411/2c99b437-3135-4453-bfab-5f756cd6751c)

### Number of Lives

You can adjust the number of lives by updating the default value for the num_lives paramter in the Hangman class constructor. 
The default number of lives you start with is 5.



![Screenshot 2024-05-22 at 17 11 40](https://github.com/gilesncwilliams/hangman_project/assets/150936411/cfb9ecd5-fafe-44c1-84b3-1806d73d501a)


## Game Rules 

- Try guessing a letter from the word chosen by the computer.
- If you guess correctly your letter will be added to the word.
- The word with your correct guess will be displayed in terminal.
  
![Screenshot 2024-05-22 at 17 16 35](https://github.com/gilesncwilliams/hangman_project/assets/150936411/01e6701c-eff5-4142-a053-f9e7f04e8b5b)

- For every wrong guess you lose a life. Once you have reached zero lives the game is over and you have lost.
- To win simply guess the word before your lives run out!
  
![Screenshot 2024-05-22 at 17 18 30](https://github.com/gilesncwilliams/hangman_project/assets/150936411/6827fb26-1df4-411a-9048-09ddaa22842b)

## File Structure

.
├── hangman                 # folder containing python files
│   ├── hangman_game.py     # final version of the game
│   ├── milestones          # archived python files for each milestone of the project 
├── .gitignore                  
└── README.md


## License Information
This repo is unlicensed as it was intended only for training purposes.
