def get_items(prompt):
    items = []
    while True:
        item = input(prompt)
        if item == '':
            break
        items.append(item)

    return items


def display_fruit(fruits):
    print("Fruits:")
    for fruit in fruits:
        print(f' - {fruit}')


def display_vegetables(veggies):
    print("Vegetables:")
    for veg in veggies:
        print(f' - {veg}')


def advice(fruits, veggies):
    if len(fruits) > len(veggies):
        display_fruit(fruits)
        display_vegetables(veggies)
        print("You need more vegetables!")

    elif len(fruits) < len(veggies):
        display_vegetables(veggies)
        display_fruit(fruits)
        print("You need more fruit!")


    else:
        display_fruit(fruits)
        display_vegetables(veggies)
        print("What a healthy balanced diet!")

def main():
    fruits = get_items("Enter a Fruit: ")
    veggies = get_items("Enter a Vegetable: ")
    advice(fruits, veggies)


if __name__ == '__main__':
    main()
