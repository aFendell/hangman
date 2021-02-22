def check_win(secret_word, old_letters_guessed):
    """
    This function checks if the player guessed the entire secret_word.
    :param secret_word: The secret word the player needs to guess.
    :param old_letters_guessed: The letters the player had already guessed.
    :type: secret_word: str
    :type: old_letters_guessed: list
    :return: True if all the letters of the secret_word are in the
             old_letters_guessed list. Else it returns False
    :rtype: bool
    """
    win = ""
    for ch in secret_word:
        if ch in old_letters_guessed:
            win = "yes"
            continue
        else:
            win = "no"
            break
    if win == "yes":
        return True
    elif win == "no":
        return False


def main():
    secret_word = "friends"
    old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
    print(check_win(secret_word, old_letters_guessed))

    secret_word = "yes"
    old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
    print(check_win(secret_word, old_letters_guessed))

    secret_word = "song"
    old_letters_guessed = ['d', 'g', 'o', 'i', 's', 'k', 'n']
    print(check_win(secret_word, old_letters_guessed))


if __name__ == '__main__':
    main()
