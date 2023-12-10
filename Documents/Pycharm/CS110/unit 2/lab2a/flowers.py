from byubit import Bit


def make_flower(bit):
    if bit.is_green():
        bit.left()
        bit.move()
        bit.right()
        bit.right()
        bit.paint("red")
        bit.move()
        bit.left()
        bit.move()


@Bit.worlds('flowers')
def go(bit):
    # Write code here
    while bit.front_clear():
        bit.move()
        make_flower(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
