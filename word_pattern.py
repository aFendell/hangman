# word pattern user input
def word_pattern(secret_word):
    print("Guess the secret word: " + str((len(secret_word) * "_ ")[:-1]))


word = "Python"


def main():
    word_pattern(word)


if __name__ == '__main__':
    main()
