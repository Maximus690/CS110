import sys
from string import punctuation


def readwords(in_file: str) -> list[str]:
    with open(in_file) as file:
        return file.read().split()


def make_dict(words_lst: list[str]) -> dict:
    dictionary = {}
    for word in words_lst:
        key, word = word_key(word)
        if key not in dictionary:
            dictionary[key] = []
        dictionary[key].append(word)
    return dictionary


def word_key(word):
    word = word.lower().strip(punctuation)
    key = (len(word), word[0])
    return key, word


def main(in_file):
    words_lst = readwords(in_file)
    dictionary = make_dict(words_lst)
    for group, items in dictionary.items():
        print(f'{group}: {items}')


if __name__ == "__main__":
    main(sys.argv[1])
