from byubit import Bit


def get_to_color(bit):
    while bit.front_clear():
        bit.move()
        if not bit.is_empty():
            paint_till_marker(bit)
            bit.snapshot('america')
    get_back(bit)
    move_up(bit)


def paint_till_marker(bit):
    color = bit.get_color()
    bit.move()
    while bit.is_empty():
        bit.paint(color)
        bit.move()


def get_back(bit):
    bit.left()
    bit.left()
    while bit.front_clear():
        bit.move()
    bit.right()


def move_up(bit):
    if bit.front_clear():
        bit.move()
        bit.right()


def destination(bit):
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


@Bit.worlds('more-lines')
def run(bit):
    while bit.front_clear():
        get_to_color(bit)
    destination(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
