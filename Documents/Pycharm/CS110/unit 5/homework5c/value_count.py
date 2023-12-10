import sys


def readlines(filename: str) -> list[str]:
    with open(filename) as file:
        return file.readlines()


def count(content, column):
    bin = {}

    for line in content:
        line = line.strip().split(',')
        info = line[int(column)]
        if info not in bin:
            bin[info] = 0
        bin[info] += 1
    return bin


def main(in_file, column):
    all_content = readlines(in_file)
    total = count(all_content, column)
    print(total)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
