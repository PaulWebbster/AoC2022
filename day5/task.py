import re


def load_data(filename):
    data = []
    with open(filename, "r") as input_file:
        for line in input_file:
            data.append(line)
    return data


def get_crates_and_their_positions(data):
    crates = []
    for pos, crate in enumerate(data[-1]):
        try:
            int(crate)
            crates.append(pos)
        except ValueError:
            continue

    return crates


def is_load(character):
    return 65 <= ord(character) <= 90


def get_load_buckets(crates, data):
    buckets = []
    for i in range(len(crates)):
        buckets.append([])

    data_length = len(data)
    for i in range(data_length, 0, -1):
        for k, j in enumerate(crates):
            try:
                a = data[i-1][j]
                if is_load(data[i-1][j]):
                    buckets[k].append(data[i-1][j])
            except IndexError:
                continue
    return buckets


def movements(data):
    regex = re.compile(r"^move (\d+) from (\d+) to (\d+)$")
    movements = []
    for line in data:
        if regex.match(line):
            groups = regex.match(line).groups()
            movements.append((int(groups[0]), int(groups[1]), int(groups[2])))

    return movements


def move_crates(movements, buckets):
    for move in movements:
        for i in range(move[0]):
            crate = buckets[move[1]-1].pop()
            buckets[move[2]-1].append(crate)


def move_crates2(movements, buckets):
    for move in movements:
        to_be_moved = buckets[move[1]-1][-move[0]:]
        for i in range(move[0]):
            buckets[move[1]-1].pop()
        buckets[move[2]-1].extend(to_be_moved)


if __name__ == '__main__':
    data = load_data('input.txt')
    crates = get_crates_and_their_positions(data[:9])
    buckets = get_load_buckets(crates, data[:8])
    movements = movements(data[10:])
    move_crates(movements, buckets)
    print(f"Answer task 1:")
    a = []
    for bucket in buckets:
        a.append(bucket[-1])
    print("".join(a))

    buckets = get_load_buckets(crates, data[:8])
    move_crates2(movements, buckets)
    print(f"Answer task 2:")
    a = []
    for bucket in buckets:
        a.append(bucket[-1])
    print("".join(a))
