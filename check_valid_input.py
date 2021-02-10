# Check valid input


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


def main():
    old_letters = ['a', 'b', 'c']
    print(check_valid_input('C', old_letters))
    print(check_valid_input('ep', old_letters))
    print(check_valid_input('$', old_letters))
    print(check_valid_input('s', old_letters))

if __name__ == '__main__':
    main()
