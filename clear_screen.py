from os import system, name
from time import sleep


HANGMAN_PHOTOS = {1: """     x-------x
     |/      |
     |
     |
     |
     |
    ============
    """,
                  2: """     x-------x
     |/      |
     |       0
     |
     |
     |
    ============
    """,
                  3: """     x-------x
     |/      |
     |       0
     |       |
     |
     |
    ============
    """,
                  4: """     x-------x
     |/      |
     |       0
     |      /|
     |
     |
    ============
    """,
                  5: """     x-------x
     |/      |
     |       0
     |      /|\\
     |
     |
    ============
    """,
                  6: """     x-------x
     |/      |
     |       0
     |      /|\\
     |      /
     |
    ============
    """,
                  7: """     x-------x
     |/      |
     |       0
     |      /|\\
     |      / \\
     |
    ===========
        LOSE
     GAME OVER"""}


def clear():
    """
    This function clears the screen.
    :param: none
    :return: none
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def main():

    print(HANGMAN_PHOTOS[1])
    sleep(3)
    clear()
    print(HANGMAN_PHOTOS[2])
    sleep(3)
    clear()
    print(HANGMAN_PHOTOS[3])
    sleep(3)
    clear()
    print(HANGMAN_PHOTOS[4])
    sleep(3)
    clear()
    print(HANGMAN_PHOTOS[5])
    sleep(3)
    clear()
    print(HANGMAN_PHOTOS[6])
    sleep(3)
    clear()
    print(HANGMAN_PHOTOS[7])
    sleep(3)

    input("\n\nPress enter to exit")


if __name__ == '__main__':
    main()
