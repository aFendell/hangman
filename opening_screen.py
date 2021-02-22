# Hangman opening screen version 2
def opening_screen():
    """
    This function prints the opening screen of the hangman game - 'Hangman'
    writen in ASCII art and the number of failed attempts the user gets.
    :param: none
    :return: none
    """
    HANGMAN_ASCII_ART = """      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/"""
    MAX_TRIES = 6

    print(HANGMAN_ASCII_ART)
    print(MAX_TRIES)


def main():
    opening_screen()


if __name__ == "__main__":
    main()
