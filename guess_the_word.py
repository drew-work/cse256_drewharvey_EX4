# Drew Harvey
# CIS256 Fall 2024
# Ex 4

import random

def choose_word():
    # Define a list of words to choose from
    word_list = ["cookie", "monster", "retreat", "labour", "completition"]
    # Select a random word from the list
    return random.choice(word_list)

def display_word(word, guessed_letters):
    # Show the word with guessed letters revealed, others as underscores
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def guess_the_word():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Set the number of attempts

    print("Welcome to Guess the Word!\n")
    print("The word to guess is:", display_word(word, guessed_letters))

    while attempts > 0:
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
            print(f"Attempts remaining: {attempts}")

        current_display = display_word(word, guessed_letters)
        print("Word:", current_display)

        if "_" not in current_display.replace(" ", ""):
            print("Congratulations! You guessed the word:", word)
            break
    else:
        print("Sorry, you've run out of attempts. The word was:", word)

# Run the game
if __name__ == "__main__":
    guess_the_word()
