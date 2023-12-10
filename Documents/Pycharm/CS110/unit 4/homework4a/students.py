def student():
    students = []
    while True:
        print("Enter a student.")
        name = input("Name: ")
        if name == '':
            break
        else:
            hometown = input("Hometown: ")
            school = input("School: ")

            students.append((name, hometown, school))
    return students


def sorting(students):
    byu = []
    other = []
    for name, hometown, school in students:
        if school == "BYU":
            byu.append((name, hometown, school))
        else:
            other.append((name, hometown, school))
    return byu, other


def main():
    students = student()
    byu, other = sorting(students)

    print("BYU Students:")
    for butt, hole, andface in byu:
        print(f"- {butt.upper()}")

    print("Other Students:")
    for butt, hole, andface in other:
        print(f"- {butt}")


if __name__ == '__main__':
    main()

