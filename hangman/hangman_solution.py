'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
from ast import Num
from curses.ascii import isalpha
import random
from unittest.mock import sentinel

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''

    word = ''
    word_guessed = []
    num_letters = 0
    num_lives = 0
    list_letters = []
   

    def __init__(self, word_list, num_lives=5):

        #assign instance variables
        self.wordlist = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for l in self.word]
        self.num_letters = len(set(self.word))

        self.word_copy = self.word
        
        print(f'The mystery word has {len(self.word)} characters" (The number of letters is NOT the UNIQUE number of letters')
        print(f'word guessed: {self.word_guessed}')

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked
        '''

        #converts the letter to lowercase
        letter = letter.lower()

        if letter in self.word and self.num_lives != 0 :
            
            if self.word_guessed != list(self.word):

                if letter in self.word_copy:

                    #search and replace letter in word guessed            
                    index = self.word_copy.index(letter)
                    self.word_guessed[index] = letter

                    #alters word to allow index() search for duplicate letters
                    l_word = list(self.word_copy)
                    l_word[index] = '_'
                    self.word_copy = ''.join(l_word)

                    # print(self.word_copy)

                #displays message
                print(f'Nice! {letter} is in the word')
                print(f'word: {self.word_guessed}')
            

                # #adds letter to list
                # self.list_letters.append(letter)

                if self.word_guessed == list(self.word):
                    #displays message
                    print("Congratulations, you won!")
                    print(f"the word is {self.word}")

                else:

                    #calls method
                    self.ask_letter()

        
        elif letter not in self.word and self.num_lives != 0:

            #reduces number of lives left
            self.num_lives -= 1

            #adds letter to list
            self.list_letters.append(letter)

            #displays message
            print(f'Sorry, {letter} is not in {self.word_guessed}')
            

            if self.num_lives != 0:

                print(f'you have {self.num_lives} live(s) left')

                #calls method
                self.ask_letter()
            
            elif self.num_lives == 0:

                #displays message
                print(f'You ran out of lives. The word was {self.word}')
                print(f'End of game!')

    def ask_letter(self) :
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''

        #user input
        letter = input("Please, enter just one alphabet: \n")

        #sentinel value 
        sentinel = 0

        #checks if letter is a single alphabet character
        while sentinel != -1:
            if (len(letter)) == 1:

                if (letter.isalpha() == True):

                   #come back to this
                    if letter not in self.list_letters :

                        #print message to user
                        print(f'You entered "{letter}"')

                        #call method
                        self.check_letter(letter)

                        #sentinel set to -1
                        sentinel = -1

                    else:

                        print(f"{letter} was already tried")

                        #prompts user to input letter
                        letter = input("Please, enter just one alphabet: \n")

                else:
                    print(f'{letter} is not an alphabet')

                    #prompts user to input letter
                    letter = input("Please, enter just one alphabet: \n")

            elif ((len(letter) != 1) or len(letter) == 1) and (letter.isalpha() != True):

                print(f'{letter} is not an alphabet')

                #prompts user to input letter
                letter = input("Please, enter just one alphabet: \n")

            else:
                
                #prompts user to input letter
                letter = input("Please, enter just one alphabet: \n")
                


def play_game(word_list): 
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
