def get_str():
    response = input("Enter a string: ")
    return str(response)


def main():
    print("Let's concatenate strings!")
    while True:
        response1 = get_str()
        response2 = get_str()
        print(f"The result is: {response1 + response2}")


if __name__ == '__main__':
    main()
