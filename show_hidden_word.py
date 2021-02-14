def show_hidden_word(secret_word, old_letters_guessed):
    """
    This function receives the secret word the player needs to guess and a list containing
    the letters the player had guessed so far. It then returns a string where the guessed
    letters are in their position (separated by 1 whitespace) and the rest of the letters are
    represented by underlines (separated by 1 whitespace)
    :param secret_word: The secret word the player needs to guess.
    :param old_letters_guessed: The letters that the player had already guessed
    :type: secret_word: str
    :type: old_letters_guessed: list
    :return: part_word_guessed: The guessed letters in their position and the un-guessed letters
    represented as underline
    :rtype: part_word_guessed: str
    """
    part_word_guessed = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            part_word_guessed += letter + " "
        else:
            part_word_guessed += "_ "
    part_word_guessed = part_word_guessed[:-1]
    print(part_word_guessed)


def main():
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    show_hidden_word(secret_word, old_letters_guessed)


if __name__ == '__main__':
    main()

