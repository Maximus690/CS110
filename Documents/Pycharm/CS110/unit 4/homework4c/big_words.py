import sys


def main(how_many: int):
    things = []
    while not len(things) == 5:
        thing = input("Word: ")
        if len(thing) >= how_many:
            things.append(thing)
        else:
            print("Too short.")

    for thing in things:
        print(f"- {thing}")


if __name__ == '__main__':
    butt = int(sys.argv[1])
    main(butt)
# Write your code here.
# Remember to use a main block.
# You can see examples of this in your lab assignments and the guide.
