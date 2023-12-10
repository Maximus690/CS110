def count_whitespace(string: str) -> int:
    total = 0
    for c in string:
        if c.isspace():
            total += 1
    return total
    #Count the number of whitespace characters in the string.


def keep_big_words(words: list[str]) -> list[str]:
    big_words_penis = []
    for word in words:
        upper = 0
        for char in word:
            if char.isupper():
                upper += 1
            if upper > 3:
                if word not in big_words_penis:
                    big_words_penis.append(word)
    return big_words_penis
    #Return a list of words with more than 3 uppercase letters.


def most_punctuation(words: list[str]) -> str:
    most_punc = float("-inf")
    max_word = None
    for word in words:
        punctuation = 0
        for c in word:
            if not c.isalnum() and not c.isspace():
                punctuation += 1
        if most_punc < punctuation:
            most_punc = punctuation
            max_word = word
    return max_word
    #Return the word with the most punctuation.


def remove_punctuation(string: str) -> str:
    result = ''
    for c in string:
        if not c.isalnum() and not c.isspace():
            c = ''
        result += c
    return result
    #Remove all punctuation from the string.


def replace_digits_with_asterisks(string: str) -> str:
    result = ''
    for c in string:
        if c.isdigit():
            c = '*'
        result += c
    return result
    #Replace all digits in the string with asterisks.
