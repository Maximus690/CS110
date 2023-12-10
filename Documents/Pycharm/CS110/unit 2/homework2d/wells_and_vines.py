from byubit import Bit


def paint_sumthin(bit,color):
    while bit.front_clear():
        bit.move()
        bit.paint(color)


def return_to_line(bit):
    bit.right()
    bit.right()
    if bit.is_green():
        while bit.front_clear():
            bit.move()
        bit.left()
    elif bit.is_blue():
        while bit.is_blue():
            bit.move()
        bit.right()


def paint_vine(bit):
    if bit.is_green():
        bit.left()
        paint_sumthin(bit, 'green')
        return_to_line(bit)


def at_well(bit):
    return bit.right_clear()


def paint_well(bit):
    if at_well(bit):
        bit.right()
        paint_sumthin(bit, 'blue')
        return_to_line(bit)


def get_to_color(bit):
    while bit.is_empty():
        bit.move()



@Bit.worlds('wells-and-vines')
def run(bit):
    # Write code here
    while bit.front_clear():
        bit.move()
        paint_vine(bit)
        paint_well(bit)



if __name__ == '__main__':
    run(Bit.new_bit)
