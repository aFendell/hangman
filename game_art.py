from colorama import init, Fore

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


def print_art(color_name, image_name):
    """
    This function receives the color and image name and prints the colored image to the screen.
    :param color_name: color to print
    :param image_name: name of the image to be printed
    :type: color_name: str
    :type: image_name: str
    :return: none
    """
    init(autoreset=True)
    color = getattr(Fore, color_name)
    print(color + GAME_IMAGES[image_name])


def main():
    print_art("GREEN", "happy")
    print_art("RED", "sad")
    print_art("YELLOW", "win")
    print_art("MAGENTA", "lose")


if __name__ == '__main__':
    main()




