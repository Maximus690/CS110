def get_opt():
    response = input("Option: ")
    return int(response)


def main():
    while True:
        print("\nwhat would you like to do?"
              "\n1) Receive compliment"
              "\n2) Receive advice"
              "\n3) Quit")
        option = get_opt()
        if option == 1:
            print("Your write the best code\n")
        if option == 2:
            print("get 8 hours of sleep every night\n")
        if option == 3:
            break


if __name__ == '__main__':
    main()
