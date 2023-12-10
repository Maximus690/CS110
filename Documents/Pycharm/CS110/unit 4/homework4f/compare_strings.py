def main():
    while True:
        word1 = input("Word 1: ")
        if word1 == "":
            break
        word2 = input("Word 2: ")

        replace = ""
        for i in range(min(len(word1), len(word2))):
            if word1[i] == word2[i]:
                replace += "*"
            else:
                replace += "."
        replace += "." * abs(len(word1) - len(word2))
        print(replace)


# why does the test pass if I don't have a way of
# printing the correct output when the words are
# different lengths? that is why I have line 14


if __name__ == "__main__":
    main()
