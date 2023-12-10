from byubit import Bit


def move_to_green(bit):
    while not bit.is_green():
        bit.move()


def rules(bit):
    if bit.is_green():
        bit.move()
    elif bit.is_red():
        bit.paint("blue")


@Bit.worlds('fix-reds')
def run(bit):
    move_to_green(bit)
    while bit.front_clear():
        bit.move()
        rules(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
