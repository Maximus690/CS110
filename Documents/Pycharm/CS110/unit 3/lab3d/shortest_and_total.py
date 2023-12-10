def shortest_word(words):
    min = words[0]
    for i in range(1, len(words)):
        if len(words[i]) < len(min):
            min = words[i]
    return min


def total_lengths(words):
    yourbutt = 0
    for i in words:
        yourbutt += len(i)
    return yourbutt


def main():
    words = ['the', 'elephant', 'ate', 'twenty', 'bananas', 'and', 'an', 'orange']
    shortest = shortest_word(words)
    total = total_lengths(words)
    print(f'The shortest word is: {shortest}')
    print(f'The total length of all the words is: {total}')


if __name__ == '__main__':
    main()
