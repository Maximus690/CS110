from byubit import Bit


def draw_one_dot(bit):
    bit.move()
    bit.left()
    bit.move()
    bit.paint('blue')
    bit.right()
    bit.right()
    bit.move()
    bit.left()
    bit.move()


@Bit.empty_world(9, 3)
def dots(bit):
    draw_one_dot(bit)
    draw_one_dot(bit)
    draw_one_dot(bit)
    draw_one_dot(bit)


if __name__ == '__main__':
    dots(Bit.new_bit)