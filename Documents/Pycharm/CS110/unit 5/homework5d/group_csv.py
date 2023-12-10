import sys
from string import punctuation


def readlines(in_file: str) -> list[str]:
    with open(in_file) as file:
        return file.readlines()


def make_dict(lst_str, key, info) -> dict:
    dictionary = {}
    for line in lst_str:
        line = line.split(",")
        group = line[int(key)]
        value = line[int(info)]
        if group not in dictionary:
            dictionary[group] = []
        dictionary[group].append(value)
    return dictionary


def main(in_file, key, info):
    lst_str = readlines(in_file)
    dictionary = make_dict(lst_str, key, info)
    for group, value in dictionary.items():
        print(f"{group}: {value}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
