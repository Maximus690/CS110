def get_player_info(jerseys):
    """
    Gets a player's name and jersey number.
    If the name is empty, returns None.
    If the jersey number is already taken, then keep asking for
    a number until an available number is entered.
    Returns a tuple of (name, number).
    """
    # Write code here
    pass


def assign_jerseys():
    """
    Signs up players and assigns jersey numbers. Uses `get_player_info`
    to get the player info until it returns None.
    Returns a list of players.
    """
    # Write code here
    pass


def print_assignments(players):
    """
    Prints a list of players using this output:
    number: name
    """
    # Write code here
    pass
        

def main():
    players = assign_jerseys()
    print_assignments(players)


if __name__ == '__main__':
    main()