def get_rating_info():
    while True:
        restaurant = input("Restaurant: ")
        if restaurant == '':
            break
        else:
            rating = input("Rating: ")
            return restaurant, float(rating)


def get_ratings():
    ratings = []
    while True:
        rating_info = get_rating_info()
        if rating_info is None:
            break
        ratings.append(rating_info)
    return ratings


def pick_highest(ratings):
    max_score = float("-inf")
    max_restaurant = None
    for restaurant, score in ratings:
        if score > max_score:
            max_score = score
            max_restaurant = restaurant

    return max_restaurant, max_score


def main():
    ratings = get_ratings()
    restaurant, score = pick_highest(ratings)
    print(f'{restaurant} is rated {score} stars.')


if __name__ == '__main__':
    main()
