import sys


def add_emojis(text, emojis):
    """Replace words in `emojis` with their corresponding symbols."""
    
    
    
if __name__ == '__main__':
    emojis = {
        'dog': '🐶',   # This one will get overwritten
        'dog': '🐕',  
        'puppy': '🐶',
        'dogs': '🐶🐶',
        'cat': '🐱',
        'tree': '🌳',
        'bird': '🐦'
    }
    print(add_emojis(sys.argv[1], emojis))
    
