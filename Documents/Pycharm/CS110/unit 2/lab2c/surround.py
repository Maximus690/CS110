from byubit import Bit


def move_to_block(bit):
    while not ready_to_paint(bit) and bit.front_clear():
        bit.move()


def ready_to_paint(bit):
    return not bit.right_clear() and not bit.is_green()


def paint_circle(bit):
    while ready_to_paint(bit):
        bit.paint("green")
        bit.move()
        if bit.right_clear():
            bit.right()
            bit.move()


@Bit.worlds('surround', 'surround2')
def run(bit):
    while bit.front_clear():
        if ready_to_paint(bit):
            paint_circle(bit)
        else:
            move_to_block(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
