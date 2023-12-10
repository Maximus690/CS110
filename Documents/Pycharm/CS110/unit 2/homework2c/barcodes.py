from byubit import Bit


def at_barcode_start(bit):
    return bit.is_blue()


def create_barcode(bit):
    bit.left()
    while bit.front_clear():
        bit.move()
        bit.paint("blue")
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


@Bit.worlds('barcode', 'barcode2')
def run(bit):
    while bit.front_clear():
        bit.move()
        if at_barcode_start(bit):
            create_barcode(bit)

if __name__ == '__main__':
    run(Bit.new_bit)

