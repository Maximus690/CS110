from byubit import Bit


def col(bit):
    bit.left()

    while bit.front_clear():
        bit.paint("green")
        bit.move()
    bit.paint("green")
    bit.right()
    bit.right()

    while bit.front_clear():
        bit.move()
    bit.left()


@Bit.worlds("grassy_field", "big_grassy_field")
def run(bit):
    while bit.front_clear():
        col(bit)
        bit.snapshot("collumn")
        bit.move()
    col(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
