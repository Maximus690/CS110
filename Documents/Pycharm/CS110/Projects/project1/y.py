from byubit import Bit


def y(bit):
    bit.paint("blue")
    bit.move()
    bit.right()
    bit.move()
    bit.left()
    bit.paint("blue")
    bit.move()
    bit.right()
    bit.move()
    bit.paint("blue")
    bit.move()
    bit.paint("blue")
    bit.move()
    bit.paint("blue")
    bit.left()
    bit.left()
    bit.move()
    bit.move()
    bit.move()
    bit.right()
    bit.move()
    bit.paint("blue")
    bit.move()
    bit.left()
    bit.move()
    bit.paint("blue")
    bit.right()
    bit.move()
    bit.move()


@Bit.worlds('y')
def paint_the_ys(bit):
    y(bit)
    bit.move()
    y(bit)


if __name__ == '__main__':
    paint_the_ys(Bit.new_bit)
