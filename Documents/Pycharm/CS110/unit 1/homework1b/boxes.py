from byubit import Bit


def red_boxes(bit):
    bit.paint("red")
    bit.move()
    bit.paint("red")
    bit.left()
    bit.move()
    bit.left()
    bit.move()
    bit.right()
    bit.right()


def blue_boxes(bit):
    bit.paint("blue")
    bit.move()
    bit.paint("blue")
    bit.left()
    bit.move()
    bit.left()
    bit.paint("blue")
    bit.move()
    bit.paint("blue")
    bit.right()
    bit.move()
    bit.right()


@Bit.worlds("boxes")
def stack_boxes(bit):
    red_boxes(bit)
    blue_boxes(bit)
    red_boxes(bit)
    blue_boxes(bit)
    red_boxes(bit)
    blue_boxes(bit)


if __name__ == '__main__':
    stack_boxes(Bit.new_bit)
