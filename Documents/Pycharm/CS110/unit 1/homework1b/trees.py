from byubit import Bit


def move_to_tree(bit):
    """ Moves to the trunk """
    bit.move()
    bit.move()
    bit.left()


def draw_trunk(bit):
    """ Draws the trunk (two red squares)  """
    bit.paint("red")
    bit.move()
    bit.paint("red")
    bit.move()


def draw_branches(bit):
    """ Draws the branches """
    bit.paint("green")
    bit.left()
    bit.move()
    bit.paint("green")
    bit.right()
    bit.move()
    bit.right()
    bit.move()
    bit.paint("green")
    bit.move()
    bit.right()
    bit.move()
    bit.paint("green")


def go_back_down(bit):
    """ Moves back down to the ground, below the right-most branch, facing right. """
    bit.move()
    bit.move()
    bit.left()


@Bit.worlds("trees")
def draw_trees(bit):
    move_to_tree(bit)
    draw_trunk(bit)
    draw_branches(bit)
    go_back_down(bit)
    bit.move()
    move_to_tree(bit)
    draw_trunk(bit)
    draw_branches(bit)
    go_back_down(bit)
    bit.move()
    move_to_tree(bit)
    draw_trunk(bit)
    draw_branches(bit)
    go_back_down(bit)


if __name__ == '__main__':
    draw_trees(Bit.new_bit)
