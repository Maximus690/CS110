

def get_books():
    books = []
    while True:
        title = input("Title: ")
        if title == '':
            break
        else:
            author = input("Author: ")
            pages = int(input("Pages: "))
            books.append((title, author, pages))
    return books


def get_author(books):
    print("Enter an author to report on.")
    author = input("Author: ")
    sum = 0
    num_books = 0
    for tuple in books:
        if tuple[1] == author:
            sum += tuple[2]
            num_books +=1
    print(f"You have read {num_books} books by {author}.")
    print(f"You have read {sum} pages by {author}.")
    return sum, num_books


def main():
    print("Enter the title, author, and pages of each book.")
    print("End with a blank title.")
    books = get_books()
    author = get_author(books)


if __name__ == '__main__':
    main()
