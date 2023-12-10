from byubit import Bit


def paint_field(bit):
    while bit.front_clear():
        col(bit)
        bit.snapshot("collumn")
        bit.move()
    col(bit)

def col(bit):
    bit.left()

    while bit.front_clear():
        bit.paint("green")
        bit.move()
    bit.paint("green")
    bit.right()
    bit.right()

    while bit.front_clear():
        bit.move()
    bit.left()


def get_to_corner(bit):
    bit.move()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


def at_exit(bit):
    return bit.right_clear()


def find_exit(bit):
    bit.left()
    while not at_exit(bit):
        bit.move()
    if at_exit(bit):
        bit.right()
        bit.move()


@Bit.worlds('soccer', 'soccer2')
def go(bit):
    while bit.front_clear():
        get_to_corner(bit)
        paint_field(bit)
        find_exit(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
