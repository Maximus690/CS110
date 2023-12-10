from byubit import Bit


def leap(bit):
    if bit.front_clear():
        bit.move()
    if bit.front_clear():
        bit.move()
    if bit.front_clear():
        bit.move()


def paint_spots(bit):
    while bit.front_clear():
        bit.paint('blue')
        leap(bit)
    bit.paint('blue')


def fill_green(bit):
    while bit.front_clear():
        bit.paint('green')
        bit.move()
    bit.paint('green')


@Bit.empty_world(6, 3)
def go(bit):
    fill_green(bit)
    bit.left()
    bit.left()
    paint_spots(bit)


if __name__ == '__main__':
    go(Bit.new_bit)