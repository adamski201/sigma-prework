import csv
import random
import time
import os

hangman_stages = [
    '''
   +---+
   |   |
       |
       |
       |
       |
=========
''',
    '''
   +---+
   |   |
   O   |
       |
       |
       |
=========
''',
    '''
   +---+
   |   |
   O   |
   |   |
       |
       |
=========
''',
    '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========
''',
    '''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========
''',
    '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========
''',
    '''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========
'''
]

MAX_MISTAKES = 6


def setup():
    answer = get_random_word_from_dictionary()

    grid = generate_answer_line(answer)

    mistakes = 0

    guessed_chars = set()

    return answer, grid, mistakes, guessed_chars


def get_formatted_hangman_from_mistakes(mistakes: int) -> str:
    return hangman_stages[mistakes]


def get_random_word_from_dictionary() -> str:
    try:
        with open("words.txt", newline="") as words:
            reader = csv.reader(words)

            word_list = list(reader)[0]

            return random.choice(word_list)

    except FileNotFoundError:
        raise Exception(
            "Words.txt not found. Ensure it is in the same directory as this file.")


def handle_guess(curr_guess: str, answer: str, answer_line: str, guessed_chars: set, mistakes: int):
    guessed_chars.add(curr_guess)

    if is_correct_guess(curr_guess, answer):
        answer_line = update_answer_line(
            curr_guess, answer, answer_line)

        return answer_line, mistakes, True
    else:
        return answer_line, mistakes+1, False


def generate_answer_line(answer: str) -> str:
    return "_" * len(answer)


def is_correct_guess(guess: str, answer: int) -> bool:
    if guess in answer:
        return True

    return False


def update_answer_line(guess: str, answer: str, answer_line: str) -> str:
    answer_line_list = list(answer_line)

    for idx, char in enumerate(answer):
        if char == guess:
            answer_line_list[idx] = char

    return ''.join(answer_line_list)


def is_valid_guess_input(input: str) -> bool:
    return len(input) == 1 and input.isalpha()


def is_unique_guess(curr_guess: str, guesses: set) -> bool:
    return curr_guess not in guesses


def is_out_of_lives(mistakes: int) -> bool:
    return mistakes >= MAX_MISTAKES


def is_won(answer_line: str, answer: str) -> bool:
    return answer_line == answer


def ask_for_guess(guessed_chars: set) -> str:
    while True:
        guess = input(
            "Enter a single character to make a guess: ").lower()

        if not is_unique_guess(guess, guessed_chars):
            print("You have already guessed this character. Please try again.")
            time.sleep(1)
            continue

        if not is_valid_guess_input(guess):
            print("Input not recognised. Please try again.")
            time.sleep(1)
            continue

        return guess


def clear_console() -> None:
    return os.system('clear')


def play_hangman() -> None:
    clear_console()

    print("Welcome to Hangman!")

    print("Guess the word by entering a single character, or try to guess the entire word itself!")

    input("Press Enter when you are ready to begin.")
    # Implement ability to type in full word instead of single character

    answer, grid, mistakes, guessed_chars = setup()

    while True:
        print(get_formatted_hangman_from_mistakes(mistakes))

        if (is_out_of_lives(mistakes)):
            print("You lose...")

            break

        print(f"Your current attempt: {grid}")

        curr_guess = ask_for_guess(guessed_chars)

        print(f"Attempting '{curr_guess}'...")

        time.sleep(1)

        grid, mistakes, is_correct = handle_guess(
            curr_guess, answer, grid, guessed_chars, mistakes)

        if is_correct:
            print("You guessed correctly!")
        else:
            print("You guessed incorrectly... you lose a life!")

        if is_won(grid, answer):
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
