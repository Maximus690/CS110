def registration():
    players = []
    while True:
        player = input("Enter player name: ")
        if player == '':
            break
        else:
            age = input("Enter player age: ")
            players.append((player, int(age)))
    return players

def sorting(players):
    big = []
    little = []
    for player, age in players:
        if age <= 10:
            little.append((player, age))
        else:
            big.append((player, age))
    return big, little


def total_members(team):
    return len(team)


def average_age(team):
    total_age = 0
    for player, age in team:
        total_age += age
    return round(total_age / len(team))


def youngest_age(team):
    min_age = None
    for player, age in team:
        if min_age is None or min_age > age:
            min_age = age
    return min_age


def oldest_age(team):
    max_age = None
    for player, age in team:
        if max_age is None or max_age < age:
            max_age = age
    return max_age


def main():
    players = registration()
    big, little = sorting(players)

    total_bigs = total_members(big)
    average_bigs = average_age(big)
    youngest_big = youngest_age(big)
    oldest_big = oldest_age(big)
    total_smalls = total_members(little)
    average_smalls = average_age(little)
    youngest_smalls = youngest_age(little)
    oldest_smalls = oldest_age(little)

    print("Team Bigs")
    print("Total members:", total_bigs)
    print("Average age:", average_bigs)
    print("Youngest age:", youngest_big)
    print("Oldest age:", oldest_big)
    print("Members")
    for butt, face in big:
        print(f" - {butt} {face}")


    print("Team Littles")
    print("Total members:", total_smalls)
    print("Average age:", average_smalls)
    print("Youngest age:", youngest_smalls)
    print("Oldest age:", oldest_smalls)
    print("Members")
    for butt, face in little:
        print(f" - {butt} {face}")


if __name__ == '__main__':
    main()
