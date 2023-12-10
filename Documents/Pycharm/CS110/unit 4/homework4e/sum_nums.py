import sys


def readlines(filename: str) -> list[str]:
    with open(filename) as file:
        return file.readlines()


def writelines(filename: str, content: list[str]):
    with open(filename, 'w') as file:
        file.writelines(content)


def buttface(lines: list[str]) -> int:
    total = 0
    for line in lines:
        total += facebutt(line)
    return total


def facebutt(line: str) -> int:
    numbers = line.split()
    total = 0
    for num in numbers:
        total += int(num)
    return total


def main(input):
    lines = readlines(input)
    # writelines(output, new_lines)
    print(f"The total is {buttface(lines)}")


if __name__ == "__main__":
    main(sys.argv[1])
# Write your code here.
# Remember to use a main block.
# You can see examples of this in your lab assignments and the guide.
