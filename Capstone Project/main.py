import csv
import random
import time
import os
import hangman


def clear_console() -> None:
    return os.system('clear')


def print_greeting() -> None:
    print("Welcome to Hangman!")

    print("Guess the word by entering a single character, or try to guess the entire word itself!")


def ask_for_guess(guessed_chars) -> str:
    while True:
        guess = input(
            "Enter a single character to make a guess: ").lower()

        if not hangman.is_unique_guess(guess, guessed_chars):
            print("You have already guessed this character. Please try again.")
            time.sleep(1)
            continue

        if not hangman.is_valid_guess_input(guess):
            print("Input not recognised. Please try again.")
            time.sleep(1)
            continue

        return guess


def play_hangman():
    clear_console()

    print_greeting()

    input("Press Enter when you are ready to begin.")
    # Implement ability to type in full word instead of single character

    answer, grid, mistakes, guessed_chars = hangman.setup()

    while True:
        print(hangman.get_formatted_hangman_from_mistakes(mistakes))

        if (hangman.is_out_of_lives(mistakes)):
            print("You lose...")

            break

        print(f"Your current attempt: {grid}")

        curr_guess = ask_for_guess(guessed_chars)

        print(f"Attempting '{curr_guess}'...")

        time.sleep(1)

        grid, mistakes, is_correct = hangman.handle_guess(
            curr_guess, answer, grid, guessed_chars, mistakes)

        if is_correct:
            print("You guessed correctly!")
        else:
            print("You guessed incorrectly... you lose a life!")

        if hangman.is_won(grid, answer):
            time.sleep(1.5)

            print("Well done, you've won!")

            break

        time.sleep(1.5)

        clear_console()

    time.sleep(1)

    play_again_input = input("Would you like to play again? (y/n): ").lower()

    if play_again_input == "y":
        play_hangman()
    else:
        exit()


def main() -> None:
    play_hangman()


if __name__ == '__main__':
    main()
