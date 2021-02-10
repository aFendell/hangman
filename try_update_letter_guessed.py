# try to update the letter_guessed list
from check_valid_input import check_valid_input


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
        print("X")
        print(old_letters_str)
        return False


def main():
    old_letters = ['s', 'p', 'o', 'f']
    try_update_letter_guessed('t', old_letters)

if __name__ == '__main__':
    main()




