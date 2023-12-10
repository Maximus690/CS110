import sys


def readfile(in_file) -> str:
    with open(in_file) as file:
        return file.read()


def buttface(string: str) -> dict:
    frequency = {}
    for char in string.lower():
        if char not in frequency:
            frequency[char] = 0
        frequency[char] += 1
    for key, value in frequency.items():
        frequency[key] = round(value/len(string), 3)
    return frequency


def main(in_file):
    string = readfile(in_file)
    frequency = buttface(string)
    print(frequency)


if __name__ == '__main__':
    main(sys.argv[1])
