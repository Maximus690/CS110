import sys


def readlines(filename: str) -> list[str]:
    with open(filename) as file:
        lines = file.readlines()
        stripped_lines = []
        for line in lines:
            stripped_lines.append(line.strip())
    return stripped_lines


def buttface(names, timeslots):
    scheduling = {}
    for name, timeslot in zip(names, timeslots):
        scheduling[name] = timeslot
    return scheduling


def facebutt(scheduling):
    while True:
        name = input("Name: ")
        if name == "":
            break

        if name in scheduling:
            timeslot = scheduling[name]
            print(f"{name} is assigned {timeslot}")
        if name not in scheduling:
            print(f"{name} is not assigned a timeslot")


def main(name, timeslot):
    names = readlines(name)
    timeslots = readlines(timeslot)
    scheduling = buttface(names, timeslots)
    facebutt(scheduling)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
