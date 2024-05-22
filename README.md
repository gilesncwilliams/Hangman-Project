# Hangman Game Project

## Introdution
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Installation Instructions
Python3 is required to run this game.

Follow these instruction to[clone a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository)).



To clone the repo to your local machine:

Above the list of files, click  Code.

Screenshot of the list of files on the landing page of a repository. The "Code" button is highlighted with a dark orange outline.
Copy the URL for the repository.

To clone the repository using HTTPS, under "HTTPS", click .

To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click .

To clone a repository using GitHub CLI, click GitHub CLI, then click .

Screenshot of the "Code" dropdown menu. To the right of the HTTPS URL for the repository, a copy icon is outlined in dark orange.
Open Terminal.

Change the current working directory to the location where you want the cloned directory.

Type git clone, and then paste the URL you copied earlier.

git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY

Step 1:
Copy the url for this repo by clicking the green 'Code' button and then copying the web URL
<img width="435" alt="Screenshot 2024-05-22 at 16 51 43" src="https://github.com/gilesncwilliams/hangman_project/assets/150936411/c7bfb5c8-5e74-4b00-818b-c3ac5d687eb4">

Step 2:


## Usage Instructions

To play the game run the Hangman_Game_Final.py script from you Command Line.

- You can also import the script and choose you're own list of words for the computer to choose from at random for you to guess from. You would just need to call the play_game(word_list) function.

- You can adjust the number of lives by updating the default value for the num_lives paramter in the Hangman class constructor.
  
- Please feel free to update the word list to include more words for the computer to choose from.

The game rules are as follows:
- Try guessing a letter for the word chosen by the computer.
- If you guess correctly your letter will be added to the word and display the word on the screen with the correcly guessed letter included. You will be able to see how many letters the word has and how many letters you have left to guess.
- You lose a life for every wrong guess. Once you have reached zero lives the game is over and you have list.
- To win simply guess the word before your lives run out!
 
## File Structure

.
├── hangman                 # folder containing python files
│   ├── hangman_game.py     # final version of the game
│   ├── milestones          # archived python files for each milestone of the project 
├── .gitignore                  
└── README.md


## License Information
This repo is unlicensed as it is intended only for training purposes.
