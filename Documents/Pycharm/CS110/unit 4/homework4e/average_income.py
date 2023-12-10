import sys


def readlines(filename: str) -> list[str]:
    with open(filename) as file:
        return file.readlines()


def buttface(lines: list[str], profession) -> list[str]:
    pro = []
    for line in lines:
        if profession in line:
            pro.append(line)
    return pro

#  list = string.split() # (',')
# string = ' '.join(list)`


def facebutt(lines: list[str], profession) -> float:
    pro = buttface(lines, profession)
    total = 0
    for item in pro:
        lit = item.split(",")
        total += int(lit[3])
    average = total/len(pro)
    return round(average)


def main(in_file, profession):
    lines = readlines(in_file)
    average = facebutt(lines, profession)
    print(f"The average income of {profession} is {average}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

# Write your code here.
# Remember to use a main block.
# You can see examples of this in your lab assignments and the guide.
