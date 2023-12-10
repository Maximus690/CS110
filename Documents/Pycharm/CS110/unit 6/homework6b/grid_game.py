import sys

BLOCKED = '*'
EMPTY = '.'
WIN = '!'


def print_grid(grid: list[list[str]]):
    """
    Print the grid with spaces between each value and newlines between each row
    """
    for row in grid:
        for item in row:
            print(item, end=' ')
        print()


def read_grid(filename: str) -> list[list[str]]:
    with open(filename) as file:
        lines = file.readlines()
    grid = []
    for line in lines:
        grid.append(line.split())
    return grid


def update_grid(grid, old_row: int, old_col: int, new_row: int, new_col: int, empty=None):
    """
    Move the value at old_row, old_col to new_row, new_col

    Fill with cell at old_row, old_col with the empty value
    """
    grid[new_row][new_col] = grid[old_row][old_col]
    grid[old_row][old_col] = empty


def is_blocked(grid, row: int, col: int, blocked_value: str):
    """
    Return True if the value at row, col in the grid is the blocked_value

    Also return True if the row, col coordinate is out of bounds.
    """
    if row < 0 or row >= len(grid):
        return True
    if col < 0 or col >= len(grid[row]):
        return True
    return grid[row][col] == blocked_value


def play(grid: list[list[str]]):
    row = 0
    col = 0
    while True:
        print_grid(grid)
        action = input('Action: ')
        if not action:
            break

        action = action.lower()
        new_row = row
        new_col = col

        if action[0] == 'u':
            if not is_blocked(grid, row - 1, col, blocked_value=BLOCKED):
                new_row = row - 1

        elif action[0] == 'd':
            if not is_blocked(grid, row + 1, col, blocked_value=BLOCKED):
                new_row = row + 1

        elif action[0] == 'l':
            if not is_blocked(grid, row, col - 1, blocked_value=BLOCKED):
                new_col = col - 1

        elif action[0] == 'r':
            if not is_blocked(grid, row, col + 1, blocked_value=BLOCKED):
                new_col = col + 1

        elif action[0] == 'q':
            break

        if row != new_row or col != new_col:
            if grid[new_row][new_col] == WIN:
                update_grid(grid, row, col, new_row, new_col, empty=EMPTY)
                print_grid(grid)
                print('You win!')
                break
            else:
                update_grid(grid, row, col, new_row, new_col, empty=EMPTY)
                row = new_row
                col = new_col


def main(filename: str):
    grid = read_grid(filename)
    play(grid)


if __name__ == '__main__':
    main(sys.argv[1])
