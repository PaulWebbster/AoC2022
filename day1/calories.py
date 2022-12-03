
def load_data(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(line)
    return data


def count_calories(data):
    elfs = []
    e = []
    for d in data:
        if d != "\n":
            e.append(int(d))
        else:
            elfs.append(sum(e))
            e = []
    return elfs


def found_leader_calories(elves_calories):
    return max(elves_calories)


def found_three_leaders_sum(elves_calories):
    sum_of_three = 0
    for i in range(3):
        max_value = max(elves_calories)
        max_i = elves_calories.index(max_value)
        elves_calories.pop(max_i)
        sum_of_three += max_value
    return sum_of_three


if __name__ == "__main__":
    calories = load_data("input.txt")
    elves = count_calories(calories)
    leader_calories = found_leader_calories(elves)
    print(f"Leader calories: {leader_calories}")
    three_leaders_sum = found_three_leaders_sum(elves)
    print(f"Sum of all calories for 3 leaders is {three_leaders_sum}")
