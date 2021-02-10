def is_index_valid(index):
    """
    This function checks if the index number entered by the user is a greater then 0 integer.
    :param index: A greater then 0 integer.
    :type: index: int
    :return: index_valid
    :rtype: bool
    """
    if index.isnumeric() and int(index) > 0:
        index_valid = True
    else:
        index_valid = False
    return index_valid


def main():
    print(is_index_valid("3"))
    print(is_index_valid("10.4"))
    print(is_index_valid("-22"))
    print(is_index_valid("0"))
    print(is_index_valid(""))


if __name__ == '__main__':
    main()
