from os import path


def path_input():
    """
    This function receives from the user the path to a text file.
    It then checks that the file exists and returns the path.
    :param: self
    :return: file_path
    :rtype: file_path: str
    """
    file_path = ""
    path_valid = False
    while not path_valid:
        # Ask user to type a file path
        file_path = input("Please type a file path and press enter: ")
        # check if path is valid
        if path.isfile(file_path):
            path_valid = True
        else:
            print("File does not exist! Make sure to type a valid file path.")
    return file_path


def index_input():
    """
    This function receives from the user a word number to select.
    It verifies that the number is an integer, greater then 0.
    :param: self
    :return: index: The number of the word the user wants to select.
    :rtype: index: int
    """
    index = ""
    index_valid = False
    while not index_valid:
        # Ask user to select a word number
        index = input("Please select a word number and press enter: ")
        # check if user entered an integer greater then 0
        if index.isnumeric() and int(index) > 0:
            index_valid = True
        else:
            print("Word number is not valid! Make sure to type an integer greater then 0.")
    return int(index)


def choose_word(file_path, index):
    """
    This function receives:
    1. The file path of a text file (str) containing words separated by whitespaces.
    2. An index number (int) representing the position of a word.
    It returns the word in the index position.
    :param file_path: The path to a text file containing words separated by whitespace.
    :type: str
    :param index: An index number representing the position of a word.
    :type: int
    :return: chosen_word: The word in the index position.
    :rtype: str
    """
    # open file for reading
    with open(file_path, "r") as file:
        words_str = file.read()
        # split string of words into a list
        words_list = words_str.split(" ")
    # choose index word
    # if index is larger then list, run loop on list
    index -= 1
    while index >= len(words_list):
        index -= len(words_list)
    chosen_word = words_list[index]
    return chosen_word


def main():
    file_path = path_input()
    index = index_input()

    print(choose_word(file_path, index))


if __name__ == '__main__':
    main()


