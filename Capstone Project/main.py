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


def get_formatted_hangman_from_mistakes(mistakes) -> str:
    return hangman_stages[mistakes]


def get_random_word_from_dictionary() -> str:
    with open("words.txt", newline="") as words:
        reader = csv.reader(words)

        word_list = list(reader)[0]

        random_idx = random.randint(0, len(word_list) - 1)

        return word_list[random_idx]


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


def clear_console() -> None:
    return os.system('clear')


def main() -> None:
    clear_console()

    print("Welcome to Hangman!")

    input("Press Enter when you are ready to begin.")
    # Add instructions here
    # Implement ability to type in full word instead of single character
    # Add fail state

    answer = get_random_word_from_dictionary()

    curr_answer_line = generate_answer_line(answer)

    mistakes = 0

    guessed_chars = set()

    while True:
        print(hangman_stages[mistakes])

        if (mistakes == 6):
            print("You lose...")
            break

        print(f"Your current attempt: {curr_answer_line}")

        # Validate input
        while True:
            curr_guess = input(
                "Enter a single character to make a guess: ").lower()

            if not is_unique_guess(curr_guess, guessed_chars):
                print("You have already guessed this character. Please try again.")
                time.sleep(1)
                continue

            if not is_valid_guess_input(curr_guess):
                print("Input not recognised. Please try again.")
                time.sleep(1)
                continue

            break

        print(f"Attempting '{curr_guess}'...")

        time.sleep(1)

        guessed_chars.add(curr_guess)

        if is_correct_guess(curr_guess, answer):
            print("You guessed correctly!")

            curr_answer_line = update_answer_line(
                curr_guess, answer, curr_answer_line)

        else:
            print("You guessed incorrectly... you lose a life!")

            mistakes += 1

        time.sleep(2)

        print("\n")
        clear_console()

    exit()


if __name__ == '__main__':
    main()
