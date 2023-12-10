from byubit import Bit


def fill(bit):
    bit.left()
    while bit.is_empty():
        bit.paint("red")
        bit.move()
    bit.paint("red")
    bit.right()
    bit.right()

    while bit.front_clear():
        bit.move()
    bit.left()


@Bit.worlds("banner", "another_banner")
def banner(bit):
    while bit.front_clear():
        fill(bit)
        bit.move()
    fill(bit)

if __name__ == '__main__':
    banner(Bit.new_bit)
