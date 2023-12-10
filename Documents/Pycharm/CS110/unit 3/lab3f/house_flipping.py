def profit(house):
    address, purchase_price, after_repair_value, cost_to_repair, project_duration = house
    monthly_property_taxes = purchase_price / 1000
    cost_of_sale = 3000
    costs = purchase_price + cost_to_repair
    costs += monthly_property_taxes * project_duration
    costs += cost_of_sale
    return after_repair_value - costs


def print_house(house):
    address, purchase_price, after_repair_value, cost_to_repair, project_duration = house
    print(f"Expected profit: {profit(house)}\n"
          f"\n"
          f"Address: {address}\n"
          f"Purchase price: {purchase_price}\n"
          f"After repair value: {after_repair_value}\n"
          f"Cost to repair: {cost_to_repair}\n"
          f"Project duration: {project_duration}\n")


def get_houses():
    houses = []
    while True:
        address = input("Address: ")
        if address == '':
            break
        else:
            purchase_price = float(input("Purchase price: "))
            after_repair_value = float(input("After repair value: "))
            cost_to_repair = float(input("Cost to repair: "))
            project_duration = float(input("Project duration: "))
            print("")
            houses.append((address, purchase_price, after_repair_value, cost_to_repair, project_duration))
    return houses


def get_best_house(houses):
    max_profit = float("-inf")
    max_house = None
    for house in houses:
        if profit(house) > max_profit:
            max_house = house
            max_profit = profit(house)
    return max_house


def main():
    houses = get_houses()
    max_house = get_best_house(houses)
    print_house(max_house)


if __name__ == '__main__':
    main()
