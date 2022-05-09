import random
from words import *
import string

def get_valid_word(words):
    word = random.choice(words)     # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print(f"You have {lives} lives left and you have used these letters: ", ' '.join(used_letters))

        # What the current word is
        word_list = [letter if letter in used_letters else '-' for letter in word] # using list comprehension method
        print('Current word: ', ' '.join(word_list))

        # getting user input
        user_letter = input("Guess a letter : ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 # takes away a life if wrond
                print("Letter is not in word")
            
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
            
        else:
            print("Invalid character. Please try it again!")

        print("\n")
    # gets here when len(word_letters) == 0 OR lives == 0
    if lives == 0:
        print(f"Sorry you died. The word was {word}")
    else:
        print(f"You have guessed the word {word} correctly")

hangman()