def no_stock():
    out = []
    print("What items are out of stock?")
    while True:
        zero_stock = input("Item: ")

        if zero_stock == "":
            break
        out.append(zero_stock)
    return out


def get_item(out):
    item_needed = []
    print("What items would you like to purchase?")
    while True:
        item = input("Item: ")
        if item in out:
            print(f"I'm sorry, the item {item.upper()} is out of stock.")
            continue
        if item == "":
            break
        item_needed.append(item)

    return item_needed


def main():
    out = no_stock()
    item_needed = get_item(out)
    print(f"You have {len(item_needed)} items:")
    for item in item_needed:
        print(f"- {item}")



if __name__ == '__main__':
    main()
