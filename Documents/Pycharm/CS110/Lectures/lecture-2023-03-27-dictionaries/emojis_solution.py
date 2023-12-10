import sys


def add_emojis(text, emojis):
    """Replace words in `emojis` with their corresponding symbols."""
    words = text.split()
    new_words = []
    for word in words:
        if word.lower() in emojis:
            # replace
            new_words.append(emojis[word.lower()])
        else:
            # don't replace
            new_words.append(word)
        
    return ' '.join(new_words)
    
    
if __name__ == '__main__':
    emojis = {
        'dog': '🐶', 
        'puppy': '🐶',
        'dogs': '🐶🐶',
        'cat': '🐱',
        'tree': '🌳',
        'bird': '🐦'
    }
    print(add_emojis(sys.argv[1], emojis))
    
