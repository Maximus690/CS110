def get_average(ratings):
    return round(sum([tup[0] for tup in ratings])/len(ratings),1)


def get_score():
    score = []
    while True:
        scores = input("Score: ")
        if scores == '':
            break
        else:
            comment = input("Comment: ")
            score.append((float(scores), comment))
    return score


def main():
    print("Enter ratings for this class.\n"
          "Each rating includes a score and a comment.\n"
          "Use a blank score to end.")
    score = get_score()
    print(f"Average rating: {get_average(score)}")
    print("Comments:")
    for penis in score:
        print("- " + penis[1])


if __name__ == '__main__':
    main()
