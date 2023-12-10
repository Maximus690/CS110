import sys

simple_codex = {
 'a': 'd',
 'b': 'e',
 'c': 'z',
 'd': 'h',
 'e': 'g',
 'f': 's',
 'g': 'n',
 'h': 'r',
 'i': 'a',
 'j': 'b',
 'k': 'k',
 'l': 'j',
 'm': 'c',
 'n': 'u',
 'o': 'y',
 'p': 't',
 'q': 'q',
 'r': 'x',
 's': 'w',
 't': 'v',
 'u': 'p',
 'v': 'f',
 'w': 'i',
 'x': 'l',
 'y': 'm',
 'z': 'o'
}


def encode(codex, message):
    result = ""
    for char in message:
        new_char = char
        if char.lower() in codex:
            new_char = codex[char.lower()]
        if char.isupper():
            new_char = new_char.upper()
        result += new_char
    return result


def main(message, codex):
    encoded = encode(codex, message)
    print(encoded)
    
    
if __name__ == '__main__':
    main(sys.argv[1], simple_codex)
    
