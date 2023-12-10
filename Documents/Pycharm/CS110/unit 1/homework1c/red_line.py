from byubit import Bit


def bita(bit):
    while not bit.is_red():
        bit.move()
    bit.right()
    bit.move()


def line(bit):
    while not bit.is_red():
        bit.paint("red")
        bit.move()
    bit.right()


def finish(bit):
    while bit.left_clear():
        bit.move()


@Bit.worlds('red-line')
def draw_line(bit):
    bita(bit)
    line(bit)
    finish(bit)


if __name__ == "__main__":
    draw_line(Bit.new_bit)
