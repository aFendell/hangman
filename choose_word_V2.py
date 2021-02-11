from os import path


def path_input():
    """
    This function receives from the user the path to a text file.
    It then checks that the file exists and returns the path.
    :param: self
    :return: file_path
    :rtype: file_path: str
    """
    file_path = input("Please enter a file path: ")
    path_valid = False
    while not path_valid:
        if path.isfile(file_path):
            path_valid = True
        else:
            print("File does not exist!")
            file_path = input("Please make sure to enter a valid file path: ")

    return file_path


def index_input():
    """
    This function receives from the user a word number to select.
    It verifies that the number is an integer, greater then 0.
    :param: self
    :return: word_num: The number of the word the user wants to select.
    :rtype: word_num: int
    """
    # Ask user to select a word number
    index = input("Please select a word number: ")
    # verify that user entered an integer greater then 0
    num_valid = False
    while not num_valid:
        if index.isnumeric() and int(index) > 0:
            num_valid = True
        else:
            index = input("Make sure to enter an integer greater then 0: ")

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
    :return: It returns a tuple with two elements: Number of unique words in the file, the word in the index position.
    """
    # open file for reading
    with open(file_path, "r") as file:
        words_str = file.read()
        # split string of words into a list
        words_list = words_str.split(" ")
        unique_list = []
        # run word by word and add unique words to list
        for word in words_list:
            if word not in unique_list:
                unique_list.append(word)
        # choose index word. if index is larger then list, run loop on list
        if index > len(words_list):
            chosen_word = str(words_list[index - 1 - len(words_list)])
        else:
            chosen_word = str(words_list[index - 1])

    return chosen_word


def main():
    file_path = path_input()
    index = index_input()

    print(choose_word(file_path, index))


if __name__ == '__main__':
    main()


