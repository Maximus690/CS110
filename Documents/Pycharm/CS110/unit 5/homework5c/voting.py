import sys


def count_votes(prompt):
    votes = {}

    while True:
        vote = input(f"{prompt}: ")
        if vote == "":
            break
        if vote in votes:
            votes[vote] += 1
        else:
            votes[vote] = 1

    return votes


def main(prompt):
    result = count_votes(prompt)
    print(result)


if __name__ == '__main__':
    main(sys.argv[1])
# Write your code here.
# Remember to use a main block.
# You can see examples of this in your lab assignments and the guide.
