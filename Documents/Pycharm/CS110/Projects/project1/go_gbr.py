from byubit import Bit


def goto_green(bit):
    while not bit.is_green():
        bit.paint("green")
        bit.move()
    bit.right()
    bit.move()


def goto_blue(bit):
    while not bit.is_blue():
        bit.paint("blue")
        bit.move()
    bit.left()
    bit.move()


def goto_red(bit):
    while not bit.is_red():
        bit.paint("red")
        bit.move()


@Bit.worlds("go-go-go", "og-og-og")
def go_gbr(bit):
    goto_green(bit)
    goto_blue(bit)
    goto_red(bit)


if __name__ == '__main__':
    go_gbr(Bit.new_bit)
