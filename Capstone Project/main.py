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

    answer = hangman.get_random_word_from_dictionary()

    curr_answer_line = hangman.generate_answer_line(answer)

    mistakes = 0

    guessed_chars = set()

    print(answer)

    while True:
        print(hangman.get_formatted_hangman_from_mistakes(mistakes))

        if (hangman.is_out_of_lives(mistakes)):
            print("You lose...")
            break

        print(f"Your current attempt: {curr_answer_line}")

        curr_guess = ask_for_guess(guessed_chars)

        print(f"Attempting '{curr_guess}'...")

        time.sleep(1)

        guessed_chars.add(curr_guess)

        if hangman.is_correct_guess(curr_guess, answer):
            print("You guessed correctly!")

            curr_answer_line = hangman.update_answer_line(
                curr_guess, answer, curr_answer_line)

        else:
            print("You guessed incorrectly... you lose a life!")

            mistakes += 1

        if hangman.is_won(curr_answer_line, answer):
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
