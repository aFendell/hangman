# try to update the letter_guessed list


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    This function checks the validity of the users input.
    It returns 'True' if:
    1. The str 'letter_guessed' is 1 character only.
    2. The str 'letter_guessed' is an alphabetical character.
    3. The str 'letter_guessed' is a letter that is not already in the list 'old_letters_guessed'.
    Else it returns 'False'
    :param letter_guessed
    :param old_letters_guessed:
    :type: letter_guessed: str
    :type: old_letter_guessed: list
    :return: True or False
    :rtype: bool
    """
    if len(letter_guessed) == 1\
            and letter_guessed.isalpha()\
            and letter_guessed not in old_letters_guessed:
        return True
    else:
        return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    This function tries to add the new 'letter_guessed' to the list of the 'old_letters_guessed'.
    If the letter is valid, meaning 1 alphabetical letter, that is not in the 'old_letters_guessed' list yet,
    the function will add the new letter to the list and return a 'True' value.
    If the letter is not valid, it will print the 'letter_guessed' as a capital,
    and underneath it will print the 'old_letters_guessed' list as lower case letters,
    separated with little arrows. It will also return a 'False' Value.
    :param letter_guessed: The new character entered by the user.
    :param old_letters_guessed: The old letters that were entered by the user.
    :type: letter_guessed: str
    :type old_letters_guessed: a list of strings
    :return: 'True' if character fit criteria and added. Else return 'False'.
    :rtype: bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed += [letter_guessed]
        return True
    else:
        old_letters_str = " -> ".join(sorted(old_letters_guessed))
        print("\nX")
        if old_letters_guessed:
            print(old_letters_str + "\n")
        return False


def main():
    old_letters = ['s', 'p', 'o', 'f']
    try_update_letter_guessed('t', old_letters)
    print(old_letters)
    try_update_letter_guessed('s', old_letters)
    try_update_letter_guessed('ep', old_letters)
    try_update_letter_guessed('$', old_letters)
    try_update_letter_guessed('7', old_letters)


if __name__ == '__main__':
    main()




