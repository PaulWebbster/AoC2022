#
# Advent of Code 2022 - Day 4 - Task 1 & 2
#

def load_data(filename):
    data = []
    with open(filename) as f:
        for line in f:
            if '\n' in line:
                data.append((line[:-1].split(',')))
            else:
                data.append(line[:].split(','))
    return data


def build_decks_list_for_each_pair(data):
    decks = []
    for pair in data:
        first = pair[0].split('-')
        second = pair[1].split('-')
        first_elfs_decks = [i for i in range(int(first[0]), int(first[1])+1)]
        second_elfs_decks = [i for i in range(int(second[0]), int(second[1])+1)]
        decks.append((first_elfs_decks, second_elfs_decks))
    return decks


def check_pairs(decks, func=all):
    k = 0
    for first, second in decks:
        if func(elem in first for elem in second):
            k += 1
            continue
        elif func(elem in second for elem in first):
            k += 1
    return k


def get_inclusive_pairs(decks):
    return check_pairs(decks, func=all)


def get_overlaping_pairs(decks):
    return check_pairs(decks, func=any)


if __name__ == '__main__':
    data = load_data('input.txt')
    decks = build_decks_list_for_each_pair(data)
    k = 0
    inclusive_pairs = get_inclusive_pairs(decks)
    overlapping_pairs = get_overlaping_pairs(decks)
    print(f"There are {inclusive_pairs} inclusive pairs and {overlapping_pairs} overlapping pairs.")