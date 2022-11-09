# hangman game
As a final proyect i developed this proyect where i can apply all my knowelge adquired in the course. so you will learn how to apply in practice the next topics of python:
- neasted dicts and lists 
- comprehensions dicts and lists
- lambda functions 
- high order functions 
- handle errors with exceptions
- CRUD files

and more topics like:

- text data cleaning
- Terminal user interface for games
- logic of a game 

## about hangman game 
Hangman is a guessing game for two or more players. computer create a word and you  guees it. you have 5 lifes. you can check the global score. 

### fast use
1. install python and the libraries of requirements.txt
2. open hanging_game.py and enjoy :)


### how the code works
1. preProcessData.py is used for scrape the file data/data.txt to find words to use in the game. you cant upload your own text from books page without worry of cleaning that. the code clean and choose only good words to play. 
    
    a. the cleaned words will be saved in data/dict_of_words.json group by number of letters
  
    note: dict_of_words.json is full of words from pinocho´s tale by default
  
2. hanging_game.py will use dict_of_words.json to show you diferents levels depends of the amount of words. the program will choose a random word, with the leght you chose.
3. the program will run until you press "ctrl+z" to exit. 

### Requirements
create a virtualenv, activate it and install the libraries from requirements.txt

