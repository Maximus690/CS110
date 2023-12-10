import sys, random


def readlines(filename: str) -> list[str]:
    with open(filename) as file:
        lines = file.readlines()
        stripped_lines = []
        for line in lines:
            stripped_lines.append(line.strip())
    return stripped_lines


def buttface(random_word, number):
    num_of_guess = 0
    while num_of_guess < number:

        num_of_guess += 1
        guess = input(f"Guess # {num_of_guess}: \n")
        facebutt(random_word, guess)
        if guess == random_word:
            print("Way to go!")
            break
    else:
        print(f'Maybe next time. The answer is {random_word}.')


def facebutt(random_word, guess):
    replace = ""
    for c1, c2 in zip(random_word, guess):
        if c1 == c2:
            replace += "!"
        elif c2 in random_word:
            replace += "?"
        else:
            replace += "*"
    replace += "*" * abs(len(random_word) - len(guess))
    print(replace)


def main(in_file, number):
    words = readlines(in_file)
    random_word = random.choice(words)
    buttface(random_word, number)


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
# Write your code here.
# Remember to use a main block.
# You can see examples of this in your lab assignments and the guide.
