from byubit import Bit


def bit_to_red(bit):
    while not bit.is_red():
        bit.paint("green")
        bit.move()
    bit.left()
    bit.move()


def bit_to_lake(bit):
    while not bit.is_blue():
        bit.paint("green")
        bit.move()


@Bit.worlds('go-to-lake', 'go-to-another-lake')
def go(bit):
    bit_to_red(bit)
    bit_to_lake(bit)


if __name__ == "__main__":
    go(Bit.new_bit)
