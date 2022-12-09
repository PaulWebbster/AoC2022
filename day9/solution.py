def load_data(filename):
    data = []
    with open(filename, "r") as input_data:
        for line in input_data:
            splitted_line = line.split(" ")
            data.append((splitted_line[0], int(splitted_line[1])))
    return data


move_vector = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (1, 0),
    "D": (-1, 0),
}


def move_head(movement, head_curr_position, tail_curr_position):
    mv_vec = move_vector[movement[0]]
    steps = movement[1]
    tail_positions = []
    for i in range(steps):
        head_prev_position = head_curr_position
        head_curr_position = head_curr_position[0] + mv_vec[0], head_curr_position[1] + mv_vec[1]
        if abs(tail_curr_position[0] - head_curr_position[0]) > 1 or abs(tail_curr_position[1] - head_curr_position[1]) > 1:
            tail_curr_position = head_prev_position
            tail_positions.append(tail_curr_position)

    return tail_positions, head_curr_position, tail_curr_position


def move_head2(movement, head_curr_position, knots):
    mv_vec = move_vector[movement[0]]
    steps = movement[1]
    tail_positions = set()

    for i in range(steps):
        prev_head_position = head_curr_position
        head_curr_position = head_curr_position[0] + mv_vec[0], head_curr_position[1] + mv_vec[1]
        knots[0] = update_knot_position(knots[0], (head_curr_position, prev_head_position))

        for j in range(8):
            knots[j+1] = update_knot_position(knots[j+1], knots[j])

        tail_positions.add(knots[8][0])

    return tail_positions, head_curr_position


def update_knot_position(knot_pos, prev_knot_pos):
    curr_prev_knot_pos = prev_knot_pos[0]
    new_pos = [*knot_pos[0]]
    prev_pos = knot_pos[1]
    if abs(knot_pos[0][0] - curr_prev_knot_pos[0]) + abs(knot_pos[0][1] - curr_prev_knot_pos[1]) >= 3:
        new_pos[0] += 1 if curr_prev_knot_pos[0] > knot_pos[0][0] else -1
        new_pos[1] += 1 if curr_prev_knot_pos[1] > knot_pos[0][1] else -1
    elif abs(knot_pos[0][0] - curr_prev_knot_pos[0]) > 1:
        new_pos[0] += 1 if curr_prev_knot_pos[0] > knot_pos[0][0] else -1
    elif abs(knot_pos[0][1] - curr_prev_knot_pos[1]) > 1:
        new_pos[1] += 1 if curr_prev_knot_pos[1] > knot_pos[0][1] else -1
    return (new_pos[0], new_pos[1]), prev_pos


if __name__ == "__main__":
    movements_data = load_data("input.txt")
    head_cur_pos = (0, 0)
    tail_cur_pos = (0, 0)
    tail_positions = set()
    tail_positions.add(tail_cur_pos)
    for mv in movements_data:
        new_tail_positions, head_cur_pos, tail_cur_pos = move_head(mv, head_cur_pos, tail_cur_pos)
        tail_positions.update(new_tail_positions)

    print(f"Task 1: {len(tail_positions)}")

    # Task 2
    knots = []
    head_cur_pos = (0, 0)
    for i in range(9):
        knots.append(((0, 0),(0,0)))

    tail_positions = set()
        
    for mv in movements_data:
        new_tail_positions, head_cur_pos = move_head2(mv, head_cur_pos, knots)
        tail_positions.update(new_tail_positions)
    print(f"Task 2: {len(tail_positions)}")
