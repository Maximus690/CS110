from byubit import Bit


def get_to_color(bit):
    while bit.front_clear():
        bit.move()
        if not bit.is_empty():
            make_bar(bit)

def return_to_bottom(bit):
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


def make_bar(bit):
    color = bit.get_color()
    bit.left()
    while bit.front_clear():
        bit.move()
        bit.paint(color)
    return_to_bottom(bit)


@Bit.worlds('color-bars', 'color-bars2')
def run(bit):
    if not bit.is_empty():
        make_bar(bit)
    while bit.front_clear():
        get_to_color(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
