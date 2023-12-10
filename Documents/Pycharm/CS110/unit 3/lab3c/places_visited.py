def get_places():
    items = []
    while True:
        response = input('Enter a place: ')
        if response == '':
            break
        items.append(response)

    return items


def print_places_visited(places_visited):
    print("I have visited:")
    for element in places_visited:
        print(f"- {element}")


def main():
    places_visited = get_places()
    print_places_visited(places_visited)


if __name__ == '__main__':
    main()
