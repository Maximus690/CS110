import sys
from encode import readlines


def writelines(out_file, content):
    with open(out_file, "w") as file:
        file.writelines(content)


def make_key_dict(key_lines: list[str]) -> dict:
    key_dict = {}
    for line in key_lines:
        line = line.strip().split(",")
        normal, random = line
        key_dict[random] = normal
    return key_dict


def decode_function(need_decode: list[str], key_dict) -> list[str]:
    decoded_lst = []
    for line in need_decode:
        decoded_line = ""
        for c in line:
            new_c = key_dict.get(c.lower(), c)
            if c.isupper():
                decoded_line += new_c.upper()
            else:
                decoded_line += new_c
        decoded_lst.append(decoded_line)
    return decoded_lst


def main(key_file, in_file, out_file):
    key_lines = readlines(key_file)
    need_decode = readlines(in_file)
    key_dict = make_key_dict(key_lines)
    decode = decode_function(need_decode, key_dict)
    writelines(out_file, decode)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])

