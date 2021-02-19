# Hangman Game
from opening_screen import opening_screen
import choose_word
from print_hangman import print_hangman
import game_art
from try_update_letter_guessed import try_update_letter_guessed
from show_hidden_word import show_hidden_word
import check_win
from clear_screen import clear
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
    # set variables
    old_letters_guessed = []
    num_of_tries = 1
    # game starts
    print("\nGuess the secret word, or you'll be hanged!")
    input("\n\nPress enter to start\n\n")
    clear()
    # run a loop for max 6 failed attempts
    while num_of_tries < 7:
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
                game_art.print_green("happy")
                # check if win
                if check_win.check_win(secret_word, old_letters_guessed):
                    show_hidden_word(secret_word, old_letters_guessed)
                    sleep(2)
                    clear()
                    game_art.print_yellow("win")
                    break
            # failed attempt
            else:
                num_of_tries += 1
                game_art.print_red("sad")
    # reached max tries - Game over
    if num_of_tries == 7:
        print_hangman(num_of_tries)
        show_hidden_word(secret_word, old_letters_guessed)
        sleep(2)
        clear()
        game_art.print_magenta("lose")
    # exit game
    input("\n\nPress enter to exit\n\n")


if __name__ == "__main__":
    main()



