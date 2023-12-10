from byubit import Bit


def at_pool(bit):
    return bit.right_clear()


def paint_pool_collumn(bit):
    bit.right()
    while bit.front_clear():
        if bit.front_clear():
            bit.move()
            bit.paint("blue")
    bit.left()
    bit.left()
    while bit.is_blue():
        bit.move()
    bit.right()
    bit.move()


def paint_pool(bit):
    while at_pool(bit):
        paint_pool_collumn(bit)


def paint_dumbass_tree(bit):
    bit.left()
    bit.paint("green")
    bit.move()
    bit.paint("green")
    bit.move()
    bit.paint("red")
    bit.left()
    bit.move()
    bit.paint("red")
    bit.right()
    bit.move()
    bit.right()
    bit.move()
    bit.paint("red")
    bit.move()
    bit.right()
    bit.move()
    bit.paint("red")
    bit.right()
    bit.move()
    bit.left()
    bit.move()
    bit.move()
    bit.left()


@Bit.worlds('blossoms', 'blossoms2')
def go(bit):
    while bit.front_clear():
        bit.move()
        if at_pool(bit):
            paint_pool(bit)
            bit.snapshot('pool')
            paint_dumbass_tree(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
