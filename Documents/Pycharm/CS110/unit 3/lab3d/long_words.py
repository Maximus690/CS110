def long_words(words):
    return [word for word in words if len(word) > 5]


def print_words(words):
    for word in words:
        print(f"- {word}")


def main():
    words = ['completely', 'fun', 'program', 'to', 'write', 'hahaha']
    long = long_words(words)
    print_words(long)


if __name__ == '__main__':
    main()
