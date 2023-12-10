import sys
from string import punctuation


def readlines(in_file) -> list[str]:
    with open(in_file) as file:
        return file.read().split()


def create_dict(words):
    dict = {}
    for num in range(1, 21):
        dict[num] = 0
    return dict


def update_dict(dictionary, words):
    for word in words:
        word_length = len(word.strip(punctuation))
        dictionary[word_length] += 1
    return dictionary


def main(in_file):
    words = readlines(in_file)
    dictionary = create_dict(words)
    new_dict = update_dict(dictionary, words)
    print(new_dict)


if __name__ == "__main__":
    main(sys.argv[1])
