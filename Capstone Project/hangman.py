import csv
import random
import time

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


def get_formatted_hangman_from_mistakes(mistakes) -> str:
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


def handle_guess(curr_guess, answer, answer_line, guessed_chars, mistakes):
    guessed_chars.add(curr_guess)

    if is_correct_guess(curr_guess, answer):
        curr_answer_line = update_answer_line(
            curr_guess, answer, answer_line)
    else:
        mistakes += 1

    return curr_guess, answer, answer_line


def generate_answer_line(answer) -> str:
    return "_" * len(answer)


def is_correct_guess(guess, answer) -> bool:
    if guess in answer:
        return True

    return False


def update_answer_line(guess, answer, answer_line):
    answer_line_list = list(answer_line)

    for idx, char in enumerate(answer):
        if char == guess:
            answer_line_list[idx] = char

    return ''.join(answer_line_list)


def is_valid_guess_input(input) -> bool:
    return len(input) == 1 and input.isalpha()


def is_unique_guess(curr_guess, guesses) -> bool:
    return curr_guess not in guesses


def is_out_of_lives(mistakes) -> bool:
    return mistakes >= MAX_MISTAKES


def is_won(answer_line, answer):
    return answer_line == answer
