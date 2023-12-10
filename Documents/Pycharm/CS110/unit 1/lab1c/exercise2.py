from byubit import Bit


@Bit.worlds('red-spot')
def go(bit):
    while not bit.is_red():
        bit.move()

    bit.left()
    bit.move()
    bit.left()

    while bit.front_clear():
        bit.move()
        bit.paint('blue')


if __name__ == '__main__':
    go(Bit.new_bit)
