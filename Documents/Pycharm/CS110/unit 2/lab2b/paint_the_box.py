from byubit import Bit


def good_to_paint(bit):
    return not bit.is_green() and bit.front_clear()


@Bit.worlds('paint-the-box', 'paint-another-box')
def run(bit):
    # Write code here
    while good_to_paint(bit):
        bit.paint("green")
        bit.move()
        if not bit.front_clear():
            bit.left()


if __name__ == '__main__':
    run(Bit.new_bit)
