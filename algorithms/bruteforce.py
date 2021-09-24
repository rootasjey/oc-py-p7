import csv


def brute_force():
    """Brute force algorythm"""
    MAX_MONEY = 500
    CURRENT_MONEY = MAX_MONEY

    print(f"MAX_MONEY = {MAX_MONEY}")
    print(f"CURRENT_MONEY = {CURRENT_MONEY}")
    print("-------")

    total_profit = 0
    all_actions = []
    chosen_actions = []

    with open("data/dataset1.csv", newline="") as csv_file:
        spamreader = csv.reader(csv_file, delimiter=',', quotechar='|')
        for row in spamreader:

            if is_action_row(row):
                action_row = format_action_row(row)
                all_actions.append(action_row)

        all_actions.sort(key=takeThird, reverse=True)

        print("-------")
        chosen_actions = choose_actions(all_actions, CURRENT_MONEY, MAX_MONEY)
        
        print(f"Picked {len(chosen_actions)} actions")
        print("-------")
        print(chosen_actions)
        print("-------")


        total_cost = 0

        for chosen_action in chosen_actions:
            cost = chosen_action[1]
            total_cost += cost

        print(f"TOTAL COST: {total_cost}")
        
        total_profit = make_profit(chosen_actions)
        print(f"TOTAL PROFIT: {total_profit}")



def make_profit(actions):
  """Calculate profit"""
  total_profit = 0

  for action in actions:
    action_profit = action[2]
    total_profit += action_profit

  return total_profit

def choose_actions(actions, money, max_money):
    """Pick actions"""
    actions_len = len(actions)
    cursor = 0

    chosen_actions = []

    while money > 0 and cursor < (actions_len - 1):
        curr_action = actions[cursor]

        # Check if enough money to buy this action
        action_cost = curr_action[1]

        future_money = money - action_cost

        if (future_money >= 0):
          chosen_actions.append(curr_action)
          money -= action_cost

        cursor += 1

    return chosen_actions


def is_action_row(data):
    """Check if the row has int values."""
    has_int_values = False
    has_float_values = False

    for value in data:
        try:
          if '.' in value:
            maybe_float = float(value)
          
            if isinstance(maybe_float, float):
                has_float_values = True

          else: 
            maybe_int = int(value)

            if isinstance(maybe_int, int):
                has_int_values = True
        except:
            "This value is not an int."

    return has_int_values or has_float_values


def format_action_row(data):
    """Check value and convert string values to int"""
    formatted_data = []
    formatted_data.append(data[0])

    cost = 0
    benefice_percent = 0

    if '.' in data[1]:
      cost = float(data[1])
    else:
      cost = int(data[1])

    if '.' in data[2]:
      benefice_percent = float(data[2])
    else:
      benefice_percent = int(data[2])

    formatted_data.append(cost)
    formatted_data.append(benefice_percent)

    benefice = cost * benefice_percent / 100
    formatted_data.append(benefice)

    return formatted_data


# take second element for sort
def takeThird(elem):
    return elem[3]
