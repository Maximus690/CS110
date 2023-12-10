def play(secret_word):
    while True:
        response = input(str("Guess a word: "))
        if response < secret_word:
            print("Higher!")
        elif response > secret_word:
            print("Lower!")
        else:
            print("You got it!")
            break


if __name__ == '__main__':
    play('python')
