def main():
    blocked = input("Characters to block: ")
    replacement = input("Replacement: ")
    while True:
        word = input("Word: ")
        if word == "":
            break
        for c in blocked:
            word = word.replace(c.lower(), replacement)
            word = word.replace(c.upper(), replacement)
        print(word)


if __name__ == '__main__':
    main()
