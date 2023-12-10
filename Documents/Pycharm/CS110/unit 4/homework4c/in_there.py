import sys


def main(word):
    guess = ""
    while True:
        guess = input("Guess: ")
        if guess == "":
            break
        elif word == guess:
            print("You got it!")
            break
        elif word in guess:
            print("It's in there...")
        else:
            print("Nope.")


if __name__ == '__main__':
    word = sys.argv[1]
    main(word)
# Write your code here.
# Remember to use a main block.
# You can see examples of this in your lab assignments and the guide.
