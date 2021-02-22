from os import system, name
from time import sleep


def clear():
    """
    This function clears the screen.
    :param: none
    :return: none
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def main():
    print("Python")
    sleep(2)
    clear()
    print("is")
    sleep(2)
    clear()
    print("a")
    sleep(2)
    clear()
    print("simple")
    sleep(2)
    clear()
    print("language")
    sleep(2)
    clear()

    input("\n\nPress enter to exit")


if __name__ == '__main__':
    main()
