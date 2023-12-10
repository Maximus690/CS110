from byubit import Bit


def wrong_green(bit):
    return not bit.right_clear() or not bit.left_clear()


@Bit.worlds('clear-green', 'clear-green2')
def run(bit):
    while bit.front_clear():
        bit.move()
        if wrong_green(bit):
            bit.erase()


if __name__ == '__main__':
    run(Bit.new_bit)
