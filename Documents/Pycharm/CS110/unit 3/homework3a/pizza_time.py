def get_name():
    entered_name = input("What is your name? ")
    return entered_name


def get_kind():
    return input("What kind of pizza do you want? ")


def get_additions():
    return input("What toppings do you want? ")


def print_summary(name, kind, toppings):
    print(f"{name} wants a {kind} pizza with {toppings}!")


def pizza_time():
    print("Welcome to Papa John's!")
    name = get_name()
    kind = get_kind()
    toppings = get_additions()
    print_summary(name, kind, toppings)


if __name__ == '__main__':
    pizza_time()
