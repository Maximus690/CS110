def get_words():
    items = []
    while True:
        response = input('Word: ')
        if response == '':
            break
        items.append(response)

    return items


def print_small(word_list, boundary):
    print("These are small:")
    for element in word_list:
        if element < boundary:
            print(element)


def print_big(word_list, boundary):
    print("These are big:")
    for element in word_list:
        if element > boundary:
            print(element)


def get_boundary():
    return input("Boundary: ")


def main():
    word_list = get_words()
    boundary = get_boundary()
    print(f"You have {len(word_list)} words")
    print_small(word_list, boundary)
    print_big(word_list, boundary)


if __name__ == '__main__':
    main()
