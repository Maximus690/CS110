from byubit import Bit


def get_to_green(bit):
    return not bit.is_green()


def remove_rocks(bit):
    return bit.is_blue()


@Bit.worlds('remove-rocks', 'remove-rocks2')
def run(bit):
    while get_to_green(bit):
        bit.move()

    bit.move()

    while get_to_green(bit):
        bit.move()
        if remove_rocks(bit):
            bit.erase()

    while bit.front_clear():
        bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)
