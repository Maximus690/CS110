import sys
from build_cipher import writelines


def readlines(in_file):
    with open(in_file) as file:
        return file.readlines()



def make_key_dict(key_lines: list[str]) -> dict:
    key_dict = {}
    for line in key_lines:
        line = line.strip().split(",")
        normal, random = line
        key_dict[normal] = random
    return key_dict


def encode_function(need_encode: list[str], key_dict) -> list[str]:
    encoded_lst = []
    for line in need_encode:
        encoded_line = ""
        for c in line:
            new_c = key_dict.get(c.lower(), c)
            if c.isupper():
                encoded_line += new_c.upper()
            else:
                encoded_line += new_c
        encoded_lst.append(encoded_line)
    return encoded_lst


def main(key_file, in_file, out_file):
    key_lines = readlines(key_file)
    need_encode = readlines(in_file)
    key_dict = make_key_dict(key_lines)
    encode = encode_function(need_encode, key_dict)
    writelines(out_file, encode)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
