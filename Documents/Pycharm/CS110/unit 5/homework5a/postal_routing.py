import sys


def readlines(filename: str) -> list[str]:
    with open(filename) as file:
        return file.readlines()


def writelines(filename: str, content: list[str]):
    with open(filename, 'w') as file:
        file.writelines(content)


def buttface(lines, bins):
    new_list = []
    for line in lines:
        words = line.strip().split()
        zipcode = int(words[-1])
        new_list.append(str(bins.get(zipcode, "unknown")) + "\n")
    return new_list


def main(in_file, output):
    bins = {
        5208: 16,
        10118: 4,
        227: 76,
        12345: 1,
        84604: 25,
        84602: 25,
        20895: 82
    }
    lines = readlines(in_file)
    new_lines = buttface(lines, bins)
    writelines(output, new_lines)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

