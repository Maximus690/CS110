import sys, random, string


def writelines(out_file, content):
    with open(out_file, "w") as file:
        file.writelines(content)


def buttface() -> list[str]:
    cipher = []
    alphabet = string.ascii_lowercase
    random_alphabet = random.sample(alphabet, len(alphabet))
    for normal, rando in zip(alphabet, random_alphabet):
        cipher.append(f"{normal},{rando}\n")
    return cipher


def main(out_file):
    content = buttface()
    writelines(out_file, content)


if __name__ == "__main__":
    main(sys.argv[1])
