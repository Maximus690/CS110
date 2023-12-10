from byubit import Bit


@Bit.empty_world(5, 3)
def go(bit):
    bit.paint("red")
    bit.move()
    bit.paint("green")
    bit.move()

    while bit.front_clear():
        bit.paint("blue")
        bit.move()

    bit.paint("blue")


if __name__ == '__main__':
    go(Bit.new_bit)
