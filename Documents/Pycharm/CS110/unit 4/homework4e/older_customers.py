import sys


def readlines(filename: str) -> list[str]:
    with open(filename) as file:
        return file.readlines()


def writelines(filename: str, content: list[str]):
    with open(filename, 'w') as file:
        file.writelines(content)


def buttface(lines: list[str], min_age) -> list[str]:
    total = []
    for line in lines:
        age = facebutt(line)
        if age == 'Age' or int(age) > min_age:
            total.append(line)
    return total

#  list = string.split() # (',')
# string = ' '.join(list)`


def facebutt(line: str) -> str:
    words = line.split(',')
    age = words[2]
    return age


def main(in_file, output, age):
    lines = readlines(in_file)
    new_lines = buttface(lines, age)
    writelines(output, new_lines)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]))

# Write your code here.
# Remember to use a main block.
# You can see examples of this in your lab assignments and the guide.
