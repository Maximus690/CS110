import sys


def readfile(filename: str) -> str:
    with open(filename) as file:
        return file.read()


def count(song, letters):
    counts = {}

    for letter in letters:
        counts[letter] = 0

    for char in song.lower():
        if char in counts:
            counts[char] += 1

    return counts


def main(letters, in_file):
    song = readfile(in_file)
    letter_counts = count(song, letters)
    print(letter_counts)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

# Write your code here.
# Remember to use a main block.
# You can see examples of this in your lab assignments and the guide.
