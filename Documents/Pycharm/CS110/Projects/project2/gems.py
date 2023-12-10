from byubit import Bit


def at_pool(bit):
    return bit.right_clear()


def paint_pool_collumn(bit, color):
    bit.right()
    while bit.front_clear():
        if bit.front_clear():
            bit.move()
            bit.paint(color)
    bit.left()
    bit.left()
    while not bit.is_empty():
        bit.move()
    bit.right()
    bit.move()


def paint_pool(bit, color):
    while at_pool(bit):
        paint_pool_collumn(bit, color)


@Bit.worlds('gems', 'gems2')
def run(bit):
    color = "empty"
    while bit.front_clear():
        bit.move()
        if not bit.is_empty():
            color = bit.get_color()
            bit.erase()
        if at_pool(bit):
            paint_pool(bit, color)
            bit.snapshot('pool')


if __name__ == '__main__':
    run(Bit.new_bit)
