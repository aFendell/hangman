# Checks the validity of the input


def is_valid_input(letter_guessed):
    """
     This function checks the validity of the input from the user.
     Valid (returns True) if 1 alphabetical letter only.
     Invalid (returns False) for every other option.
     :param letter_guessed: input from the user
     :type letter_guessed: str
     :return: True if valid, False if not valid
     :rtype: bool
    """
    if len(letter_guessed) >= 2:
        return False
    elif not letter_guessed.isalpha():
        return False
    elif len(letter_guessed) == 1 and letter_guessed.isalpha():
        return True


print(is_valid_input("a"))
print(is_valid_input("A"))
print(is_valid_input("$"))
print(is_valid_input("ty"))
print(is_valid_input("wwe&"))
print(is_valid_input(" "))
print(is_valid_input("  "))

