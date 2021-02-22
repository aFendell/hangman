HANGMAN_PHOTOS = {0: """     x-------x
     |/      |
     |
     |
     |
     |
    ============
    """,
                  1: """     x-------x
     |/      |
     |       0
     |
     |
     |
    ============
    """,
                  2: """     x-------x
     |/      |
     |       0
     |       |
     |
     |
    ============
    """,
                  3: """     x-------x
     |/      |
     |       0
     |      /|
     |
     |
    ============
    """,
                  4: """     x-------x
     |/      |
     |       0
     |      /|\\
     |
     |
    ============
    """,
                  5: """     x-------x
     |/      |
     |       0
     |      /|\\
     |      /
     |
    ============
    """,
                  6: """     x-------x
     |/      |
     |       0
     |      /|\\
     |      / \\
     |
    ==========="""}


def print_hangman(num_of_tries):
    """
    This function receives the number of tries and prints out the hangman image.
    :param num_of_tries: The number of guesses the user got wrong.
    :type: num_of_tries: int
    :return: none
    :rtype: none
    """
    print(HANGMAN_PHOTOS[num_of_tries])


def main():
    print_hangman(1)
    print_hangman(2)
    print_hangman(3)
    print_hangman(4)
    print_hangman(5)
    print_hangman(6)
    print_hangman(7)


if __name__ == '__main__':
    main()

