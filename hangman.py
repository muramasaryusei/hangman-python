"""
This module implements the game of Hangman. It provides functionality for
selecting a random word from a list, processing user guesses, and determining
whether the game has been won or lost.
"""

import random
import string
from words_list import words


# defining a function to get a random word that is valid
def get_valid_word(a):
    """
    Selects a valid word from the provided list of words.

    Parameters:
    words (list): A list of words from which to select a valid word.

    Returns:
    str: A valid word from the list, converted to uppercase.
    """
    word = random.choice(a) #  picks a random word from the list of words
    while '-' in word or ' ' in word: # ! if the word contains whitespace or hyphen, loop the choice
        word = random.choice(a)
    return word.upper( ) # returns an uppercase version of the chosen word

def hangman():
    """
    This function initializes and runs the Hangman game. It selects a random word,
    sets up the game state, and handles the game loop until the game is won or lost.
    """
    word = get_valid_word(words)
    word_letters = set(word) #  creates a set of letters for the hidden word
    alphabet = set(string.ascii_uppercase) # creates a set of all alphabets
    used_letters = set() # storing the letters that the user has already guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # !👆keeps looping until there are letters in the word_letters or any lives left
        print(f'You have {lives} lives left.')
        print("You have guessed these letters: ", " ".join(used_letters))
        # ?👆The letters that are already guessed by the user is displayed

        # what current word is with hyphen (G - E S S)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if  user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 #  deducting life when wrongly guessing

        elif  user_letter in used_letters:
            print('You have already guessed the letter!!')

        else:
            print("Invalid Input")

    if lives == 0:
        print("Oh no! You died. The word was", word)
    else:
        print('You won! The word was', word)

hangman()
