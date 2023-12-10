import sys
import random


def readlines(filename: str) -> list[str]:
    with open(filename) as file:
        lines = file.readlines()
        stripped_lines = []
        for line in lines:
            stripped_lines.append(line.strip())
    return stripped_lines


def any_char_matches(word1: str, word2: str) -> bool:
    for char in word1:
        if char in word2:
            return True
    return False


def buttface(secret_word):
    word = secret_word
    while True:
        guess = input("Guess a word: ")
        if guess == "":
            break
        elif word == guess:
            print("That's it!")
            break
        elif guess in word:
            print("almost")
        elif any_char_matches(word, guess):
            print("close")
        else:
            print("nope")


def main(in_file):
    stripped_lines = readlines(in_file)
    secret_word = random.choice(stripped_lines)
    buttface(secret_word)


if __name__ == "__main__":
    main(sys.argv[1])
