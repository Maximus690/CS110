def get_items(prompt):
    items = []
    while True:
        item = input(prompt)
        if item == '':
            break
        items.append(item)

    return items


def display_with_bullet(bullet, items):
    for item in items:
        print(f'{bullet} {item}')
    print()


def main():
    items = get_items("Item: ")
    print()
    bullets = get_items('Custom Bullet Point: ')
    print()
    for bullet in bullets:
        display_with_bullet(bullet, items)


if __name__ == '__main__':
    main()
