def get_noun1():
    return input("Noun: ")


def get_adj1():
    return input("Adjective: ")


def get_adj2():
    return input("Adjective: ")


def get_noun2():
    return input("Noun: ")


def get_num():
    return input("Number: ")


def get_adj3():
    return input("Adjective: ")


def get_ptverb():
    return input("Past-Tense Verb: ")


def get_game():
    return input("Game: ")


def get_verb():
    return input("Verb: ")


def mad_libs():
    print("Welcome to Mad Libs!")
    print("Please enter the following words:")
    noun1 = get_noun1()
    adj1 = get_adj1()
    adj2 = get_adj2()
    noun2 = get_noun2()
    number = get_num()
    adj3 = get_adj3()
    ptverb = get_ptverb()
    game = get_game()
    verb = get_verb()
    print(f"Once upon a time a student at found themselves in a {noun1} class. The teacher was so {adj1} "
          f"that the student started to daydream about a {noun2}. Then the "
          f"student woke up and realized that they were still in class. The teacher was "
          f"so {adj2} that they gave the student a {number} on the assignment. The student "
          f"was so {adj3} that he {ptverb} the class and went home to play {game}. The "
          f"moral of the story is that you should never {verb} in class.")


if __name__ == '__main__':
    mad_libs()
