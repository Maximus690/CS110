def change_excuse(proverb):
    """
    Change: A bad excuse is better than none.
    To: Every good excuse is worth millions.
    """
    proverb = proverb.replace('A', 'Every')
    proverb = proverb.replace('bad', 'good')
    proverb = proverb.replace('better than', 'worth')
    proverb = proverb.replace('none', 'millions')
    return proverb


def change_mountain(proverb):
    """
    Change: Do not make a mountain out of a mole hill.
    To: You should make a lemonade out of those lemons!
    """
    # Write code here
    pass


def change_fire(proverb):
    """
    Change: Fight fire with fire.
    To: Fight Thanos with a lightsaber.
    """
    # Write code here
    pass


def change_late(proverb):
    """
    Change: Better late than never.
    To: Always late and never sorry!
    """
    # Write code here
    pass


def change_your_own(proverb):
    # Write code here
    pass

def main():
    print(change_excuse('A bad excuse is better than none.'))
    print(change_mountain('Do not make a mountain out of a mole hill.'))
    print(change_fire('Fight fire with fire.'))
    print(change_late('Better late than never.'))
    # Find proverbs here:
    # https://en.wikipedia.org/wiki/List_of_proverbial_phrases
    print(change_your_own('Put a phrase here'))


if __name__ == '__main__':
    main()
