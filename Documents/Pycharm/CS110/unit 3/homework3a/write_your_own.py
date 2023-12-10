def get_name():
    return input("What is your name? ")


def get_order():
    return input("What do you want? ")


def get_side():
    return input("What side would you like? ")


def print_summary(name, order, side):
    print(f"{name} wants {order}, with {side}!")


def main():
    print("Welcome to Chick-fil-a!")
    name = get_name()
    order = get_order()
    side = get_side()
    print_summary(name, order, side)


if __name__ == '__main__':
    main()
