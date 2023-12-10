from byubit import Bit


def cross_blue(bit):
    return bit.is_green()


def turn_left(bit):
    return not bit.right_clear() and not bit.front_clear()


def end_condition(bit):
    return not bit.right_clear() and not bit.left_clear() and not bit.front_clear()


def turn_right(bit):
    return not bit.left_clear() and not bit.front_clear()


def paint(bit):
    if cross_blue(bit):
        bit.paint("blue")
    else:
        bit.paint("green")


@Bit.worlds('scurry', 'scurry2')
def go(bit):
    while not end_condition(bit):
        paint(bit)
        if turn_left(bit):
            bit.left()
            bit.move()

        elif turn_right(bit):
            bit.right()
            bit.move()

        else:
            bit.move()
    bit.paint("green")


if __name__ == '__main__':
    go(Bit.new_bit)
