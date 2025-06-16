"""
snowman.py

Main entry point for the Snowman Meltdown game.

This module initializes and manages the full game loop. It selects a random word,
displays the snowman ASCII art based on the number of incorrect guesses, and processes
user input until the word is guessed or the snowman melts. The game includes input
validation, a replay option, and extended ASCII art stages for smoother transitions.

Functions:
- get_random_word: Selects a random word from the word list.
- get_valid_input: Ensures input is a valid, new single alphabetical character.
- display_game_state: Displays current snowman stage, word progress, and guessed letters.
- play_game: Manages the interactive gameplay loop with win/loss conditions.
- main: Entry point to start the game with replay functionality.

Author: Martin Haferanke
Date: 16.06.2025
"""

import random
import re

from config.config import STAGES, WORDS
from typing import List


def get_random_word() -> str:
    """
    Selects a random word from the predefined list of words.

    :return: A randomly chosen word.
    :rtype: str
    """
    return random.choice(WORDS)


def get_valid_input(guessed_letters: List[str]) -> str:
    """
    Prompts the user until a valid, new single letter is entered.

    :param guessed_letters: List of already guessed letters.
    :type guessed_letters: List[str]
    :return: A valid single lowercase letter.
    :rtype: str
    """
    while True:
        guess = input("Guess a letter: ").lower().strip()
        if not re.fullmatch(r"[a-zA-Z]", guess):
            print("Invalid input. Please enter a single letter (a-z).")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess


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
    print("\n" + "=" * 30)
    print(STAGES[min(mistakes, len(STAGES) - 1)])
    print("Mistakes:", mistakes, "/", len(STAGES) - 1)

    display_word = ""
    for letter in secret_word:
        display_word += letter + " " if letter in guessed_letters else "_ "
    print("Word:", display_word.strip())
    print("Guessed letters:", " ".join(sorted(guessed_letters)))

    # A little divider
    print("=" * 30 + "\n")


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
        guess = get_valid_input(guessed_letters)
        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print("Incorrect!")

        game_won = all(letter in guessed_letters for letter in secret_word)

        if game_won:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("🎉 Congratulations! You saved the snowman!\n")
            break

        if mistakes >= max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"💥 Oh no! The snowman melted! The word was: '{secret_word}'\n")
            break


def main() -> None:
    """
    Entry point for starting the game.

    :return: None
    """
    while True:
        play_game()
        replay = input("Play again? (y/n): ").lower().strip()
        if replay != "y":
            print("Thanks for playing Snowman Meltdown! ❄️")
            break


if __name__ == "__main__":
    main()
