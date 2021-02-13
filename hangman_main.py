# Hangman Game
from opening_screen_V2 import opening_screen
import choose_word_V2
from print_hangman import print_hangman
from word_pattern import word_pattern
from check_valid_input import check_valid_input
from try_update_letter_guessed import try_update_letter_guessed
from show_hidden_word import show_hidden_word
from check_win import check_win


def main():
    # Present 'Hangman' opening screen
    opening_screen()
    # Ask user to enter file_path and check if file exists
    file_path = choose_word_V2.path_input()
    # Ask user to enter an index number to select a word
    index = choose_word_V2.index_input()
    # Choose a secret word
    secret_word = choose_word_V2.choose_word(file_path, index)
    # Present the 1st 'Hangman' image
    print_hangman(1)
    # Present the secret_word pattern
    word_pattern(secret_word)

    old_letters_guessed = []
    num_of_tries = 1
    # run a loop for max 6 failed attempts
    while num_of_tries < 7:
        # Ask user to guess a single letter and press enter
        ch = (input("Please guess a single alphabetic letter: ")).lower()
        # Check if character is valid - single english letter and not already in the old_letters_guessed list
        # If not valid print 'X' and the old letters guessed separated with arrows
        if not check_valid_input(ch, old_letters_guessed):
            try_update_letter_guessed(ch, old_letters_guessed)
            continue
        else:
            # If valid, update 'old_letters_guessed' list
            try_update_letter_guessed(ch, old_letters_guessed)
            # If not in secret_word - failed attempt - print next step of 'Hangman'
            if ch not in secret_word:
                num_of_tries += 1
                print(":(")
                print_hangman(num_of_tries)
            else:
                # Check for win - guessed all letters of secret_word
                if check_win(secret_word, old_letters_guessed):
                    show_hidden_word(secret_word, old_letters_guessed)
                    print("Win")
                    break
            # Print partial secret_word
            show_hidden_word(secret_word, old_letters_guessed)

    if num_of_tries == 7:
        print("\n    LOSE ! ! !\n    GAME OVER ! ! !")


if __name__ == "__main__":
    main()

