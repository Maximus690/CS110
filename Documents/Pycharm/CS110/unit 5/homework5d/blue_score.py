import sys
from string import punctuation


def input_loop():
    lst = []
    while True:
        phrase = input("Phrase: ")
        if phrase == "":
            break
        lst.append(phrase)
    return lst


def blue_score_dict(lst_phrases: list[str]) -> dict:
    blue_dict = {}
    for phrase in lst_phrases:
        blue_score = calculate_blue_score(phrase)
        if blue_score not in blue_dict:
            blue_dict[blue_score] = []
        blue_dict[blue_score].append(phrase)
    return blue_dict


def calculate_blue_score(phrase: str) -> int:
    blue_words = ["byu", "cougar", "cougars", "blue"]
    total = 0
    for word in phrase.split():
        if word.lower().strip(punctuation) in blue_words:
            total += 1
    return total


def main():
    lst_phrases = input_loop()
    blue_dict = blue_score_dict(lst_phrases)
    for blue_score, phrases in blue_dict.items():
        print(f"{blue_score}:")
        for phrase in phrases:
            print(phrase)
        print()


if __name__ == "__main__":
    main()
