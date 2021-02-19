from colorama import Fore, init

GAME_IMAGES = {
    "happy": """
     .-^^^^^^-.
   .'          '.
  /   O      O   \\
 :                :
 : ',          ,' :
  \\  '-......-'  /
   '.          .'
     '-......-'
     """, "sad": """
     .-^^^^^^-.
   .'          '.
  /   O      O   \\
 :           `    :
 :    .------.    :
  \\  '        '  /
   '.          .'
     '-......-'
     """, "win": """
            __          _______ _   _   _
            \\ \\        / /_   _| \\ | | | |
             \\ \\  /\\  / /  | | |  \\| | | |
              \\ \\/  \\/ /   | | | . ` | | |
               \\  /\\  /   _| |_| |\\  | |_|
                \\/  \\/   |_____|_| \\_| (_)
   _____ _____  ______       _______        _  ____  ____    _ 
  / ____|  __ \\|  ____|   /\\|__   __|      | |/ __ \\|  _ \\  | |
 | |  __| |__) | |__     /  \\  | |         | | |  | | |_) | | |
 | | |_ |  _  /|  __|   / /\\ \\ | |     _   | | |  | |  _ <  | |
 | |__| | | \\ \\| |____ / ____ \\| |    | |__| | |__| | |_) | |_|
  \\_____|_|  \\_\\______/_/    \\_\\_|     \\____/ \\____/|____/  (_)
    """, "lose": """
                 _     ___  ____  _____ 
                | |   / _ \\/ ___|| ____|
                | |  | | | \\___ \\|  _|  
                | |__| |_| |___) | |___ 
                |_____\\___/|____/|_____|
   ____    _    __  __ _____    _____     _______ ____  
  / ___|  / \\  |  \\/  | ____|  / _ \\ \\   / / ____|  _ \\ 
 | |  _  / _ \\ | |\\/| |  _|   | | | \\ \\ / /|  _| | |_) |
 | |_| |/ ___ \\| |  | | |___  | |_| |\\ V / | |___|  _ < 
  \\____/_/   \\_\\_|  |_|_____|  \\___/  \\_/  |_____|_| \\_\\
    """}


# def print_art(color,image_name):
#     """
#     This function receives the image name and prints it on the screen.
#     :param image_name: name of the image to be printed
#     :type: image_name: str
#     :return: none
#     """
#     print(Fore. + GAME_IMAGES[image_name])


def print_green(image_name):
    init(autoreset=True)
    print(Fore.GREEN + GAME_IMAGES[image_name])


def print_red(image_name):
    init(autoreset=True)
    print(Fore.RED + GAME_IMAGES[image_name])


def print_yellow(image_name):
    init(autoreset=True)
    print(Fore.YELLOW + GAME_IMAGES[image_name])


def print_magenta(image_name):
    init(autoreset=True)
    print(Fore.MAGENTA + GAME_IMAGES[image_name])


def main():
    print_green("happy")
    print_red("sad")
    print_yellow("win")
    print_magenta("lose")


if __name__ == '__main__':
    main()


