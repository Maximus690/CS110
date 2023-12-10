import sys


def readlines(filename: str) -> list[str]:
    with open(filename) as file:
        return file.readlines()


def writelines(filename: str, content: list[str]):
    with open(filename, 'w') as file:
        file.writelines(content)


def buttface(lines, bullet_bob):
    buttface = []
    for line in lines:
        line = bullet_bob + " " + line
        buttface.append(line)
    return buttface


def main(input, output, bullet_bob):
    lines = readlines(input)
    new_lines = buttface(lines,bullet_bob)
    butt = writelines(output, new_lines)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
# Write your code here.
# Remember to use a main block.
# You can see examples of this in your lab assignments and the guide.
