def get_verb():
    items = []
    while True:
        response = input('Enter a verb ending in "ing": ')
        if response == '':
            break
        items.append(response)

    return items


def print_puppy_libs(places_visited):
    for element in places_visited:
        print(f"The puppy is {element}!")
    print("The puppy is taking a nap")


def main():
    puppy_libs = get_verb()
    print_puppy_libs(puppy_libs)


if __name__ == '__main__':
    main()
