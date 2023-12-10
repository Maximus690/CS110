import sys


def cut_lines(lines):
    cut_lines = []
    for line in lines:
        cut_lines.append(line.split())
    return cut_lines


def state_in_line(line_data, state):
    return state in line_data


def filter_for_state(data, state):
    keepers = []
    for line_data in data:
        if state_in_line(line_data, state):
            keepers.append(line_data)
    return keepers


def get_unemployment(data_line):
    return float(data_line[3])


def find_greatest(state_data):
    biggest = None
    for data_line in state_data:
        if biggest is None or get_unemployment(data_line) > get_unemployment(biggest):
            biggest = data_line
    return biggest


def main(filename, state):
    lines = readlines(filename)
    data = cut_lines(lines)
    stat_data = filter_for_state(data,state)
    max_line = find_greatest(state_data)
    print(' '. join(max_line))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
# :)