def double_words(words):
    return [f"{word} {word}" for word in words]


def print_words(words):
    for word in words:
        print(f"- {word}")


def main():
    words = ['really', 'very', 'so', 'crazy']
    doubled = double_words(words)
    print_words(doubled)


if __name__ == '__main__':
    main()
