def print_max_date(dates, max_cost):
    print(f"Here are all the dates below ${max_cost}:")
    for date, budget in dates:
        print(f"- {date} costs ${budget}.")


def get_dates():
    dates = []
    while True:
        date = input("Date idea: ")
        if date == '':
            break
        else:
            budget = int(input("Date cost: "))
            dates.append((date, budget))
    return dates


def get_budget_date(dates):
    max_cost = int(input("Get max cost for date: "))
    budget_dates = [(date, budget) for date, budget in dates if budget <= max_cost]

    return budget_dates, max_cost


def main():
    dates = get_dates()
    budget_date, max_cost = get_budget_date(dates)
    print_max_date(budget_date, max_cost)


if __name__ == '__main__':
    main()
