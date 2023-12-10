from byubit import Bit


def not_red_rose(bit):
    return bit.is_green() or bit.is_blue()


@Bit.worlds('red-roses', 'red-roses2')
def run(bit):
    # Write code here
    while bit.front_clear():
        bit.move()
        if not_red_rose(bit):
            bit.paint("red")


if __name__ == '__main__':
    run(Bit.new_bit)
