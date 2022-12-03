def load_backpacks():
    backpacks = []
    with open("input.txt", "r") as input_data:
        for line in input_data:
            backpacks.append(line[:-1])
    return backpacks


def convert_char_to_value(item):
    value = ord(item)
    if 97 <= value <= 122:
        value -= 96
    elif 65 <= value <= 90:
        value -= 38
    return value


def common_items(backpacks):

    common_items = []
    for backpack in backpacks:
        half_items = int(len(backpack)/2)
        comp1 = backpack[:half_items]
        comp2 = backpack[half_items:]
        for item in comp1:
            if item in comp2:
                value = convert_char_to_value(item)
                common_items.append(value)
                break
    return sum(common_items)


def badges(backpacks):
    unique_items = []
    for i in range(0, len(backpacks), 3):
        for item in backpacks[i]:
            if item in backpacks[i+1] and item in backpacks[i+2]:
                value = convert_char_to_value(item)
                unique_items.append(value)
                break
    return sum(unique_items)


if __name__ == "__main__":
    bp = load_backpacks()

    c = common_items(bp)
    print(f"Compon items sum in backpack: {c}")

    b = badges(bp)
    print(f"Backpacks badges sum is {b}")
