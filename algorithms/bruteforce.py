import csv


def brute_force():
    """Brute force algorythm"""
    MAX_MONEY = 500
    CURRENT_MONEY = MAX_MONEY

    print(f"MAX_MONEY = {MAX_MONEY}")
    print(f"CURRENT_MONEY = {CURRENT_MONEY}")
    print("-------")

    # profit = 0
    all_actions = []
    chosen_actions = []

    with open("data/dataset0.csv", newline="") as csv_file:
        spamreader = csv.reader(csv_file, delimiter=',', quotechar='|')
        for row in spamreader:

            if is_action_row(row):
                action_row = format_action_row(row)
                all_actions.append(action_row)

        all_actions.sort(key=takeThird, reverse=True)

        print("-------")
        chosen_actions = choose_actions(all_actions, CURRENT_MONEY, MAX_MONEY)
        print(chosen_actions)

        print(f"Picked {len(chosen_actions)} actions")

        total_cost = 0

        for chosen_action in chosen_actions:
            cost = chosen_action[1]
            total_cost += cost

        print(total_cost)


def choose_actions(actions, money, max_money):
    """Pick actions"""
    actions_len = len(actions)
    cursor = 0

    chosen_actions = []

    while money > 0 and cursor < (actions_len - 1):
        curr_action = actions[cursor]
        chosen_actions.append(curr_action)

        action_cost = curr_action[1]
        money -= action_cost
        cursor += 1

    return chosen_actions


def is_action_row(data):
    """Check if the row has int values."""
    has_int_values = False

    for value in data:
        try:
            maybe_int = int(value)

            if isinstance(maybe_int, int):
                has_int_values = True
        except:
            "This value is not an int."
            #print(f"{value} is not an int.")

    return has_int_values


def format_action_row(data):
    """Check value and convert string values to int"""
    formatted_data = []
    formatted_data.append(data[0])

    cost = int(data[1])
    benefice_percent = int(data[2])

    formatted_data.append(cost)
    formatted_data.append(benefice_percent)

    benefice = cost * benefice_percent / 100
    formatted_data.append(benefice)

    return formatted_data


# take second element for sort
def takeThird(elem):
    return elem[3]
