def load_trees(filename):
    forest = []
    with open(filename, 'r') as data_input:
        for line in data_input:
            line_of_trees = []
            for tree in line:
                if tree != '\n':
                    line_of_trees.append(int(tree))
            forest.append(line_of_trees)
    return forest


def is_visible_from_left(x, y, forest):
    return all([forest[y][x] > forest[y][x1] for x1 in range(x)])


def is_visible_from_right(x,y,forest):
    return all([forest[y][x] > forest[y][x1] for x1 in range(len(forest[0])-1, x, -1)])


def is_visible_from_top(x, y, forest):
    return all([forest[y][x] > forest[y1][x] for y1 in range(y)])


def is_visible_from_bottom(x, y, forest):
    return all([forest[y][x] > forest[y1][x] for y1 in range(len(forest)-1, y, -1)])


def task_1(forest):
    visible_pos = set()

    for y in range(len(forest)):
        for x in range(len(forest)):
            if (x == 0 or y == 0) or (x == len(forest[0]) - 1 or y == len(forest) - 1):
                visible_pos.add((y, x))
            elif is_visible_from_left(x, y, forest) or is_visible_from_right(x, y, forest):
                visible_pos.add((y, x))
            elif is_visible_from_top(x, y, forest) or is_visible_from_bottom(x, y, forest):
                visible_pos.add((y, x))
    
    return len(visible_pos)

def number_of_trees_visible_right(x, y, forest):
    visible_trees = 0
    for x1 in range(x+1, len(forest[0])):
        if forest[y][x1] < forest[y][x]:
            visible_trees += 1
        else:
            visible_trees += 1
            break
    return visible_trees


def number_of_trees_visible_left(x, y, forest):
    visible_trees = 0
    for x1 in range(x-1, -1, -1):
        if forest[y][x1] < forest[y][x]:
            visible_trees += 1
        else:
            visible_trees += 1
            break
    return visible_trees


def number_of_trees_visible_below(x, y, forest):
    visible_trees = 0
    for y1 in range(y+1, len(forest)):
        if forest[y1][x] < forest[y][x]:
            visible_trees += 1
        else:
            visible_trees += 1
            break
    return visible_trees


def number_of_trees_visible_up(x, y, forest):
    visible_trees = 0
    for y1 in range(y-1, -1, -1):
        if forest[y1][x] < forest[y][x]:
            visible_trees += 1
        else:
            visible_trees += 1
            break
    return visible_trees

def task_2(forest):
    scenic_view = []
    for y in range(len(forest)):
        scenic_view_row = []
        for x in range(len(forest)):
            scenic_view_row.append(number_of_trees_visible_up(x, y, forest) *
                                   number_of_trees_visible_below(x, y, forest) *
                                   number_of_trees_visible_left(x, y, forest) *
                                   number_of_trees_visible_right(x, y, forest)
            )
        scenic_view.append(scenic_view_row)

    max_value = 0
    for view in scenic_view:
        for v in view:
            if v > max_value:
                max_value = v
    return max_value


if __name__ == '__main__':
    forest = load_trees('input.txt')

    print(f"Task 1: {task_1(forest)}")
    print(f"Task 2: {task_2(forest)}")
            