from byubit import Bit


def at_clif(bit):
    return bit.right_clear() and not bit.is_blue()


def jump(bit):
    while at_clif(bit):
        bit.right()
        bit.paint("green")
        bit.move()
        bit.left()


def jump_down(bit):
    while not bit.is_blue():
        if bit.is_empty():
            bit.paint("green")
            bit.move()
        if at_clif(bit):
            jump(bit)

def swim(bit):
    while bit.front_clear():
        bit.move()
    bit.left()
    bit.move()
    bit.right()
    bit.move()


def run_red(bit):
    while bit.front_clear():
        bit.paint("red")
        bit.move()
    bit.paint("red")


@Bit.worlds('bitathon', 'bitathon2')
def run(bit):
    jump_down(bit)
    swim(bit)
    run_red(bit)



if __name__ == '__main__':
    run(Bit.new_bit)
