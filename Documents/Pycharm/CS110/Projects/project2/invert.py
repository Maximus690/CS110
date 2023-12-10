from byubit import Bit


def invert(bit):
    if bit.is_blue():
        bit.erase()
    else:
        bit.paint("blue")


def up_down_over(bit):
    bit.left()
    while bit.front_clear():
        invert(bit)
        bit.move()
        bit.snapshot("america")
    invert(bit)
    get_back(bit)
    bit.snapshot("america")
    move_over(bit)
    bit.snapshot("america")


def get_back(bit):
    bit.left()
    bit.left()
    while bit.front_clear():
        bit.move()
    bit.left()


def move_over(bit):
    if bit.front_clear():
        bit.move()


def destination(bit):
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


@Bit.worlds('invert', 'invert2')
def run(bit):
    while bit.front_clear():
        up_down_over(bit)
    up_down_over(bit)


if __name__ == '__main__':
    run(Bit.new_bit)

