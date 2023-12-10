import sys
import random


def readlines(filename: str) -> list[str]:
    with open(filename) as file:
        return file.readlines()


def buttface(lines: list[str]) -> list[str]:
    pass


def main(in_file):
    lines = readlines(in_file)
    selection = random.choice(lines)
    quote = selection.split("|")
    for i in quote:
        print(i)


if __name__ == "__main__":
    main(sys.argv[1])