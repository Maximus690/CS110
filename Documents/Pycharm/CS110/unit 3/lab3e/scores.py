def find_highest_score(scores):
    booty = None
    for tup in scores:
        if booty is None or booty[2] < tup[2]:
            booty = tup
    return booty


def main():
    scores = [('Johns', 'Hayden', 72),
              ('Rodriguez', 'Emily', 94),
              ('Young', 'Henry', 91),
              ('Bean', 'Alma', 95),
              ('Peterson', 'Roger', 83)]
    last, first, score = find_highest_score(scores)
    print(f"Highest score: {first} {last}, {score}")


if __name__ == '__main__':
    main()
