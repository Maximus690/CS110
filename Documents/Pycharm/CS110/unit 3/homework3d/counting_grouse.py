def grouse_num(prompt):
    grouse = []
    while True:
        number = input(prompt)
        if number == '':
            break
        grouse.append(int(number))
    print(f"There are {sum(grouse)} total grouse.")
    return grouse


def main():
    grouse = grouse_num("Enter an observation count: ")
    print(f"The smallest count is: {min(grouse)}")
    print(f"The largest count is: {max(grouse)}")
    factor = int(input("Enter factor: "))
    numbers = [number * factor for number in grouse]
    print("The estimated grouse populations are:")
    for number in numbers:
        print(f"- {number}")


if __name__ == '__main__':
    main()
