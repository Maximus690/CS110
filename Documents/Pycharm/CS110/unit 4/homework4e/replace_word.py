import sys


def readlines(filename: str) -> list[str]:
    with open(filename) as file:
        return file.readlines()


def writelines(filename: str, content: list[str]):
    with open(filename, 'w') as file:
        file.writelines(content)


def buttface(lines: list[str], old_word, new_word) -> list[str]:
    total = []
    for line in lines:
        new_line = facebutt(line, old_word, new_word)
        total.append(new_line)
    return total

#  list = string.split() # (',')
# string = ' '.join(list)`


def facebutt(line: str, old_word, new_word) -> str:
    words = line.split()
    total = []
    for word in words:
        if word == old_word:
            word = new_word
        total.append(word)
    total = " ".join(total)
    total += '\n'
    return total


def main(in_file, output, old_word, new_word):
    lines = readlines(in_file)
    new_lines = buttface(lines, old_word, new_word)
    writelines(output, new_lines)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
