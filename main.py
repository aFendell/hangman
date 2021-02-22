# Hangman Game
from opening_screen import opening_screen
import choose_word
from clear_screen import clear
from print_hangman import print_hangman
from show_hidden_word import show_hidden_word
from try_update_letter_guessed import try_update_letter_guessed
from game_art import print_art
import check_win
from time import sleep


def main():
    # Present 'Hangman' opening screen
    opening_screen()
    # Ask user to type a file path and check if file exists
    file_path = choose_word.path_input()
    # Ask user to select a word
    index = choose_word.index_input()
    # Choose a secret word
    secret_word = choose_word.choose_word(file_path, index)
    clear()
    # start screen
    print_art("CYAN", "large_hangman")
    print("Guess the secret word, or you'll be hanged!")
    input("\n\nPress enter to start\n\n")
    clear()
    # set variables
    old_letters_guessed = []
    num_of_tries = 0
    # run a loop for max 6 failed attempts
    while num_of_tries < 6:
        # print the hangman image
        print_hangman(num_of_tries)
        # show partial secret word
        show_hidden_word(secret_word, old_letters_guessed)
        # Ask user to guess a single letter
        ch = (input("Guess a letter: ")).lower()
        # clear screen
        clear()
        # check if letter is valid
        if try_update_letter_guessed(ch, old_letters_guessed):
            # check if letter in secret word
            if ch in secret_word:
                print_art("GREEN", "happy")
                # check if win
                if check_win.check_win(secret_word, old_letters_guessed):
                    show_hidden_word(secret_word, old_letters_guessed)
                    # print flashing win banner
                    for i in range(3):
                        sleep(1)
                        clear()
                        sleep(1)
                        print_art("YELLOW", "win")
                    break
            # failed attempt
            else:
                num_of_tries += 1
                print_art("RED", "sad")
    # reached max tries - Game over
    if num_of_tries == 6:
        print_hangman(num_of_tries)
        show_hidden_word(secret_word, old_letters_guessed)
        sleep(1)
        clear()
        # print lose banner
        print_art("MAGENTA", "lose")
    # exit game
    input("\n\nPress enter to exit\n\n")


if __name__ == "__main__":
    main()
