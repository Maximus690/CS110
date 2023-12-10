from byubit import Bit


def red_thread(bit):
    bit.left()
    bit.paint("red")
    bit.move()
    bit.paint("red")
    bit.move()
    bit.paint("red")
    bit.right()
    bit.move()

def red_thread_end(bit):
    bit.left()
    bit.paint("red")
    bit.move()
    bit.paint("red")
    bit.move()
    bit.paint("red")
    bit.right()
    bit.right()
    bit.move()
    bit.move()
    bit.left()


def green_blue_thread(bit):
    bit.paint("green")
    bit.move()
    bit.paint("green")
    bit.move()
    bit.paint("green")
    bit.right()
    bit.move()
    bit.paint("green")
    bit.move()
    bit.paint("green")
    bit.right()
    bit.move()
    bit.paint("green")
    bit.move()
    bit.paint("green")
    bit.right()
    bit.move()
    bit.paint("green")
    bit.right()
    bit.move()
    bit.paint("blue")
    bit.move()
    bit.move()
    bit.right()
    bit.move()
    bit.left()


@Bit.worlds("quilt")
def make_a_quilt(bit):
    red_thread(bit)
    green_blue_thread(bit)
    red_thread(bit)
    green_blue_thread(bit)
    red_thread(bit)
    green_blue_thread(bit)
    red_thread_end(bit)


if __name__ == '__main__':
    make_a_quilt(Bit.new_bit)
