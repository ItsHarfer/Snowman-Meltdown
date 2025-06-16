"""
snowman.py

Main entry point for the Snowman Meltdown game.

This module initializes and manages the full game loop. It selects a random word,
displays the snowman ASCII art based on the number of incorrect guesses, and processes
user input until the word is guessed or the snowman melts.

Functions:
- get_random_word: Selects a random word from the word list.
- display_game_state: Displays current snowman stage and masked word.
- play_game: Manages the interactive gameplay loop with win/loss conditions.
- main: Entry point to start the game.

Author: Martin Haferanke
Date: 16.06.2025
"""

import random
from config.config import STAGES
from typing import List


WORDS = ["python", "git", "github", "snowman", "meltdown", "coffee"]


def get_random_word() -> str:
    """
    Selects a random word from the predefined list of words.

    :return: A randomly chosen word.
    :rtype: str
    """
    return random.choice(WORDS)


def display_game_state(
    mistakes: int, secret_word: str, guessed_letters: List[str]
) -> None:
    """
    Displays the current snowman ASCII art stage and the secret word with guessed letters revealed.

    :param mistakes: The number of incorrect guesses made.
    :type mistakes: int
    :param secret_word: The word the user is trying to guess.
    :type secret_word: str
    :param guessed_letters: Letters the user has guessed so far.
    :type guessed_letters: List[str]
    :return: None
    """
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        display_word += letter + " " if letter in guessed_letters else "_ "
    print("Word:", display_word)
    print()


def play_game() -> None:
    """
    Runs the main game loop, prompting the user to guess letters,
    updating the game state, and ending the game on win or loss.

    :return: None
    """
    secret_word = get_random_word()
    guessed_letters: List[str] = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print("Incorrect!")

        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Congratulations! You saved the snowman!")
            break

        if mistakes >= max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Oh no! The snowman melted! The word was:", secret_word)
            break


def main() -> None:
    """
    Entry point for starting the game.

    :return: None
    """
    play_game()


if __name__ == "__main__":
    main()
