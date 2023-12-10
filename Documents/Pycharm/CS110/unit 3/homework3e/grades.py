
def get_scores():
    scores = []
    while True:
        student = input("Student: ")
        if student == '':
            break
        else:
            score = input("Score: ")
            scores.append((student, float(score)))
    return scores


def main():
    print("Enter scores for each student.\n"
          "Enter a blank student name to end.")
    scores = get_scores()
    bonus = float(input("Bonus: "))
    cutoff = int(input("Cutoff: "))
    print("High Scores:")
    for score in scores:
        new_score = round(score[1] *(1 + bonus),1)
        if new_score > cutoff:
            print(f"- {new_score}: {score[0]}")


if __name__ == '__main__':
    main()
