import sys


def readlines(filename: str) -> list[str]:
    with open(filename) as file:
        return file.readlines()


def writelines(filename: str, content: list[str]):
    with open(filename, 'w') as file:
        file.writelines(content)


def facebutt(line, corrections):
    new_line = []
    words = line.strip().split()

    for word in words:
        if word in corrections:
            new_line.append(corrections[word])
        else:
            new_line.append(word)

    return " ".join(new_line) + "\n"


def buttface(lines, corrections):
    new_list = []
    for line in lines:
        new_lines = facebutt(line, corrections)
        new_list.append(new_lines)
    return new_list


def main(in_file, output):
    corrections = {
        'teh': 'the',
        'adn': 'and',
        'thye': 'they',
        'yuo': 'you',
        'i': 'I'
    }
    lines = readlines(in_file)
    new_lines = buttface(lines, corrections)
    writelines(output, new_lines)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
# Write your code here.
# Remember to use a main block.
# You can see examples of this in your lab assignments and the guide.
