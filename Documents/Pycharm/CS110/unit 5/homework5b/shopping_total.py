import sys


def readlines(filename: str) -> list[str]:
    with open(filename) as file:
        lines = file.readlines()
        stripped_lines = []
        for line in lines:
            stripped_lines.append(line.strip())
    return stripped_lines


def make_dict(list):
    bin = {}
    for line in list:
        urbutt = line.split(",")
        bin[urbutt[0]] = urbutt[1]
    return bin


def facebutt(item_quant, item_price):
    total = 0
    for item, quant in item_quant.items():
        total += float(quant) * float(item_price[item])
    return round(total, 2)


def main(name, price):
    items = readlines(name)
    prices = readlines(price)
    item_quant = make_dict(items)
    item_price = make_dict(prices)
    total = facebutt(item_quant, item_price)
    print(f"The total is ${total}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
# Write your code here.
# Remember to use a main block.
# You can see examples of this in your lab assignments and the guide.
