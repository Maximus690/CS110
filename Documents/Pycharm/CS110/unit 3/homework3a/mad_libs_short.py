def get_noun1():
    return input("Noun: ")


def get_adjective():
    return input("Adjective: ")


def get_noun2():
    return input("Noun: ")


def get_character():
    return input("Character: ")


def get_animal():
    return input("Animal (Plural): ")


def mad_libs_short():
    print("Welcome to Mad Libs!")
    print("Please enter the following words:")
    noun1 = get_noun1()
    adjective = get_adjective()
    noun2 = get_noun2()
    character = get_character()
    animal = get_animal()
    print(f"{noun1} sat on a {noun2}. {noun1} had a {adjective} fall. All {character}'s {animal}"
          f" and all the {character}'s men couldn't put {noun1} together again.")


if __name__ == '__main__':
    mad_libs_short()
