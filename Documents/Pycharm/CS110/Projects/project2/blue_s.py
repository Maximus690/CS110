from byubit import Bit


def move_to_paint(bit):
    while bit.front_clear() and not bit.is_green():
        bit.move()
    if bit.is_green():
        paint_sTop(bit)
        paint_bTop(bit)


def paint_sTop(bit):
    bit.left()
    draw_line(bit)


def paint_bTop(bit):
    bit.left()
    bit.move()
    bit.right()
    draw_line(bit)
    bit.right()



def draw_line(bit):
    bit.paint("blue")
    while bit.front_clear():
        bit.move()
        bit.paint("blue")
    bit.right()
    while bit.front_clear():
        bit.move()
        bit.paint("blue")
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()
    while bit.front_clear():
        bit.move()


@Bit.worlds('blue-s', 'big-blue-s')
def run(bit):
    while bit.front_clear():
        move_to_paint(bit)



if __name__ == '__main__':
    run(Bit.new_bit)
