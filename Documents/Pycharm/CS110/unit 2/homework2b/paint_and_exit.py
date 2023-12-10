from byubit import Bit


def good_to_paint(bit):
    return not bit.right_clear() and not bit.is_blue()


def get_to_green(bit):
    return bit.front_clear() and not bit.is_green()

@Bit.worlds('paint-and-exit', 'paint-and-exit2')
def run(bit):
    while good_to_paint(bit):
        bit.paint("blue")
        bit.move()
        if not bit.front_clear():
            bit.left()

    bit.right()
    bit.right()

    while get_to_green(bit):
        bit.move()
        if not bit.front_clear():
            bit.right()



if __name__ == '__main__':
    run(Bit.new_bit)
