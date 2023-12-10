import sys


def main():
    pics = ['', '', '', '', '']

    while True:
        print(pics)
        print()
        slot_input = input("Slot: ")

        if slot_input == "":
            break

        slot = int(slot_input)
        picture = input("Pic: ")

        pics[slot] = picture


if __name__ == "__main__":
    main()
