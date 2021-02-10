# check if the file_path exists
from os import path


def is_path_valid(file_path):
    """
    This function checks if the file_path leeds to an existing file.
    If file exists, it returns 'True'.
    If file does not exists, it alerts the user and returns 'False'.
    :param file_path: A path to a file
    :type: file_path: str
    :return: path_valid
    :rtype: bool
    """
    if path.isfile(file_path):
        path_valid = True
    else:
        print("File does not exist!")
        path_valid = False
    return path_valid


def main():
    print(is_path_valid("words.txt"))
    print(is_path_valid("dodo.txt"))


if __name__ == '__main__':
    main()

