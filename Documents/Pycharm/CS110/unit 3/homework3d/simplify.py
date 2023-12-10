def get_words(prompt):
    words = []
    while True:
        word = input(prompt)
        if word == '':
            break
        words.append(word)
    return words


def get_length(prompt):
    return input(prompt)


def main():
    words = get_words("Enter a word: ")
    length = int(get_length("Enter a length: "))
    short_words = [word for word in words if len(word) <= length]
    print(f"There are {len(short_words)} short words:")
    for word in short_words:
        print(f"- {word}")


if __name__ == '__main__':
    main()
