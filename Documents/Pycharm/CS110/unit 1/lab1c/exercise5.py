from byubit import Bit


def move_until_blue(bit):
    while not bit.right_clear():
        bit.move()


def move_until_red(bit):
    while not bit.is_red():
        bit.move()


@Bit.worlds('dive-for-treasure', 'dive-for-deep-treasure')
def dive(bit):
    move_until_blue(bit)
    bit.right()
    move_until_red(bit)
    bit.paint("blue")


if __name__ == "__main__":
    dive(Bit.new_bit)
