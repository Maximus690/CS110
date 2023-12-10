from byubit import Bit


def get_to_color(bit):
    while bit.is_empty():
        bit.move()


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


@Bit.worlds('lines')
def run(bit):
    while bit.front_clear():
        get_to_color(bit)
        paint_till_marker(bit)
        get_back(bit)
        move_up(bit)
    destination(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
