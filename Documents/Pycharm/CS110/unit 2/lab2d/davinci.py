from byubit import Bit

# This change lets us draw really big pictures
import byubit

byubit.bit.MAX_STEP_COUNT = 10_000


def go_paint(bit, color):
    """Paint `color` until blocked in front"""
    while bit.front_clear():
        bit.paint(color)
        bit.move()


def run(bit, how_many):
    """Move bit `how_many` squares"""
    if how_many > 0:
        bit.move()
        run(bit, how_many - 1)


def paint_many(bit, color, how_many):
    """Paint `color` and move `how_many` times"""
    if how_many > 0:
        bit.paint(color)
        bit.move()
        paint_many(bit, color, how_many - 1)


def paint_to(bit, color, ending_color):
    """Paint `color` until you reach `ending_color`"""
    while bit.get_color() != ending_color:
        bit.paint(color)
        bit.move()


def box(bit, color, size):
    """
    Draws a 3x3 box of the specified color
    Bit starts and ends in the same position and orientation
    Bit expects that the starting square is not already the specified color
    """
    while bit.get_color() != color:
        paint_many(bit, color, size)
        bit.left()


def turn_around(bit):
    bit.left()
    bit.left()


def go(bit):
    """Go until blocked in front"""
    while bit.front_clear():
        bit.move()


def column(bit, color):
    """Fill a column with `color`"""
    bit.left()
    go_paint(bit, color)
    turn_around(bit)
    go_paint(bit, color)
    bit.left()


def fill(bit, color):
    """Fill the unblocked space with `color`"""
    column(bit, color)
    while bit.front_clear():
        bit.move()
        column(bit, color)


@Bit.empty_world(30, 20)
def draw(bit):
    fill(bit, "blue")




if __name__ == '__main__':
    draw(Bit.new_bit)
