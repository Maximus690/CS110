def calculator():
    while True:
        print("\nWhat would you like to do?"
              "\n 1) Add"
              "\n 2) Subtract"
              "\n 3) Quit")
        option = input("Option: ")
        if option == '1':
            number1 = int(input("Number 1: "))
            number2 = int(input("Number 2: "))
            print(f"{number1 + number2}")
        elif option == '2':
            number1 = int(input("Number 1: "))
            number2 = int(input("Number 2: "))
            print(f"{number1 - number2}")
        elif option == '3':
            break
        else:
            print(f"Unrecognized response: {option}")


if __name__ == '__main__':
    calculator()
