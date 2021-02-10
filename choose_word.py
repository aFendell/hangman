# Ex. 9.4.1 choose_word function
from os import path


def choose_word(file_path, index):
    """
    This function receives:
    1. The file path of a text file (str) containing words separated by whitespaces.
    2. An index number (int) representing the position of a word.
    It returns a tuple with two elements:
    1. The number of unique words in the file.
    2. The word in the index position.
    :param file_path: The path to the file containing the words.
    :type: str
    :param index: An index number (int) representing the position of a word.
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
    print(choose_word("word.txt", 7))


if __name__ == '__main__':
    main()
