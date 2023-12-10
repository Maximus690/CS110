from byubit import Bit


def get_to_color(bit):
    while bit.is_empty() and bit.front_clear():
        bit.move()


def get_to_flower_top(bit):
    if not bit.front_clear():
        return
    color = bit.get_color()
    bit.erase()
    while not bit.is_green():
        bit.move()

    bit.left()

    while not bit.is_empty():
        bit.move()

    bit.paint(color)
    bit.right()
    bit.right()

    while bit.front_clear():
        bit.move()
    bit.left()
    bit.move()


@Bit.worlds('flowers1', 'flowers2')
def run(bit):
    while bit.front_clear():
        get_to_color(bit)
        get_to_flower_top(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
