from byubit import Bit


def fill_pipe(bit):
    if bit.right_clear():
        bit.right()
        bit.move()
        bit.paint("blue")
        bit.left()
        bit.left()
        bit.move()
        bit.right()


    elif bit.left_clear():
        bit.left()
        bit.move()
        bit.paint("blue")
        bit.right()
        bit.right()
        bit.move()
        bit.left()



@Bit.worlds('fix-pipe')
def go(bit):
    while bit.front_clear():
        bit.move()
        fill_pipe(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
