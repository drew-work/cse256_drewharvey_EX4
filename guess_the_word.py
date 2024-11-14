# Drew Harvey
# CIS256 Fall 2024
# Ex 4

import random

def select_random_word():
    words = ["cookie", "monster", "retreat", "labour", "completition"]
    return random.choice(words)

def display_word_progress(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display

def guess_the_word():
    word = select_random_word()
    guessed_letters = set()
    attempts = len(word) + 5  # Allowing extra attempts
    
    print("Welcome to Guess the Word!")
    print("Try to guess the word one letter at a time.")
    
    while attempts > 0:
        print("\nWord:", display_word_progress(word, guessed_letters))
        print(f"Attempts remaining: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            attempts -= 1
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print("\nSorry, you're out of attempts. The word was:", word)

if __name__ == "__main__":
    guess_the_word()
