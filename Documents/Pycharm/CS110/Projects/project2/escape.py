from byubit import Bit


def left_turn(bit):
    return not bit.front_clear() and not bit.right_clear()


def right_turn(bit):
    return not bit.front_clear() and not bit.left_clear()


def get_to_green(bit):
    bit.paint("blue")
    bit.move()
    while bit.front_clear() and not bit.is_green():
        bit.paint("blue")
        bit.move()
        if left_turn(bit):
            bit.left()
        elif right_turn(bit):
            bit.right()


def finish_green(bit):
    while bit.is_green():
        bit.move()


def get_to_end(bit, color):
    bit.right()
    bit.move()
    bit.paint(color)
    while bit.front_clear():
        bit.move()


@Bit.worlds('escape', 'escape2')
def run(bit):
    color = bit.get_color()
    bit.snapshot('america')
    get_to_green(bit)
    bit.snapshot('america')
    finish_green(bit)
    bit.snapshot('america')
    get_to_end(bit, color)
    bit.snapshot('america')


if __name__ == '__main__':
    run(Bit.new_bit)
