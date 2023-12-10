def doubles(text):
    text = text.replace("oo", "oooooo")
    text = text.replace("ee", "eeeeee")
    return text

    # Replace all "oo" with "oooooo" and all "ee" with "eeeeee".
    # Return the new text.


def for_reals(text):
    text = text.replace("%", " percent")
    text = text.replace("!", " (for reals).")
    return text

    # Replace all '%' with ' percent' and all '!' with ' (for reals).'
    # Notice the spaces!    ^                           ^
    # Return the new text.


def only_o(text):
    vowels = ['a', 'e', 'i', 'u']
    vowels_upper = ['A', 'E', 'I', "O", "U"]
    for c in vowels:
        text = text.replace(c, 'o')
    for c in vowels_upper:
        text = text.replace(c, "O")
    return text

    # Replace all vowels (aeiou) with 'o'
    # Preserve the casing of each letter.
    # Return the new text.
    #
    # Example:
    # >>> only_o("I like to eat apples and bananas")
    # "O loko to oot opplos ond bononos"


def upper_vowels(text):
    vowels = ['a', 'e', 'i', 'u', 'o']
    for c in vowels:
        text = text.replace(c, c.upper())
    return text

    # Make all vowels uppercase.
    # Return the new text.
