

def ratings_for_flavor(ratings, requested_flavor):
    return [tuple for tuple in ratings if tuple[0] == requested_flavor]


def get_average(ratings):
    return round(sum([tup[1] for tup in ratings])/len(ratings),1)


def print_info(ratings, flavor):
    average = get_average(ratings)
    print(f"The average rating for {flavor} is {average}.")


def get_ratings():
    ratings = []
    while True:
        flav = input("Enter a flavor: ")
        if flav == '':
            break
        else:
            rating = input("Enter a rating: ")
            ratings.append((flav, float(rating)))
    return ratings



def get_flavors():
    flavs = []
    print("Enter flavors to get info on, ending with a blank line.")
    while True:
        flav = input("Flavor: ")
        if flav == '':
            break
        else:
            flavs.append(flav)
    return flavs


def main():
    ratings = get_ratings()
    flavors = get_flavors()
    for flavor in flavors:
        new_ratings = ratings_for_flavor(ratings, flavor)
        print_info(new_ratings, flavor)


if __name__ == '__main__':
    main()
