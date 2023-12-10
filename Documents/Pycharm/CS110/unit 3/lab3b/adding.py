def get_number():
    response = input("Enter a number: ")
    return int(response)



def main():
    while True:
        print("I can add numbers for you!")
        number1 = get_number()
        number2 = get_number()
        print(f"The result is: {number1 + number2}")
        response = input("Would you like to do more? ")
        if response == "no" or response == "No":
            break


if __name__ == '__main__':
    main()



