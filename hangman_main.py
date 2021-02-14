# Hangman Game
from opening_screen import opening_screen
import choose_word
from print_hangman import print_hangman
from try_update_letter_guessed import try_update_letter_guessed
from show_hidden_word import show_hidden_word
from check_win import check_win


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
    # Present the 1st 'Hangman' image
    print_hangman(num_of_tries)
    # Present the secret_word pattern
    show_hidden_word(secret_word, old_letters_guessed)
    print("Guess the secret word.")
    # run a loop for max 6 failed attempts
    while num_of_tries < 7:
        # Ask user to guess a single letter and press enter
        ch = (input("Type a single alphabetic letter: ")).lower()
        # check if letter is valid
        if try_update_letter_guessed(ch, old_letters_guessed):
            # show partial word
            show_hidden_word(secret_word, old_letters_guessed)
            # check if letter in secret word
            if ch in secret_word:
                # check if win
                if check_win(secret_word, old_letters_guessed):
                    break
            # failed attempt
            else:
                num_of_tries += 1
                print(":(")
                print_hangman(num_of_tries)
                # reached max tries - Game over
                if num_of_tries == 7:
                    print("\n    LOSE ! ! !\n    GAME OVER ! ! !")
                    break


if __name__ == "__main__":
    main()

