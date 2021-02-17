# Hangman Game
from opening_screen import opening_screen
import choose_word
from print_hangman import print_hangman
from try_update_letter_guessed import try_update_letter_guessed
from show_hidden_word import show_hidden_word
from check_win import check_win
from clear_screen import clear


def main():
    # Present 'Hangman' opening screen
    opening_screen()
    # Ask user to type a file path and check if file exists
    file_path = choose_word.path_input()
    # Ask user to select a word
    index = choose_word.index_input()
    # Choose a secret word
    secret_word = choose_word.choose_word(file_path, index)
    # set variables
    old_letters_guessed = []
    num_of_tries = 1
    # run a loop for max 6 failed attempts
    while num_of_tries < 7:
        print_hangman(num_of_tries)
        show_hidden_word(secret_word, old_letters_guessed)
        # Ask user to guess a single letter and press enter
        ch = (input("Guess a letter: ")).lower()
        # clear screen
        clear()
        # check if letter is valid
        if try_update_letter_guessed(ch, old_letters_guessed):
            # check if letter in secret word
            if ch in secret_word:
                print("\n(:\n")
                # check if win
                if check_win(secret_word, old_letters_guessed):
                    break
            # failed attempt
            else:
                num_of_tries += 1
                print("\n:(\n")
                # reached max tries - Game over
                if num_of_tries == 7:
                    print_hangman(num_of_tries)
    # exit the game
    input("\n\nPress enter to exit\n\n")


if __name__ == "__main__":
    main()



