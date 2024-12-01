import numpy as np

with open("AdventOfCode_2022/Day08/input.txt", "r") as fp:
    input = fp.readlines()


def is_visible(forrest, tree, coordinates):
    num_rows, num_cols = forrest.shape
    if is_edge_tree(num_rows, num_cols, coordinates):
        return True
    elif is_visible_from_north(forrest, coordinates, tree):
        return True
    elif is_visible_from_east(forrest, coordinates, tree):
        return True
    elif is_visible_from_south(forrest, coordinates, tree):
        return True
    elif is_visible_from_west(forrest, coordinates, tree):
        return True
    else:
        return False


def is_edge_tree(num_rows, num_cols, coordinates):
    return coordinates[0] == 0 or coordinates[1] == 0 or coordinates[0] == num_rows-1 or coordinates[1] == num_cols-1


def is_visible_in_line(line_of_trees, me):
    for tree in line_of_trees:
        if tree < me:
            pass
        else:
            return False
    return True


def is_visible_from_north(forrest, coordinates, me):
    row, col = coordinates
    line_of_trees = forrest[:row, col]
    return is_visible_in_line(line_of_trees, me)


def is_visible_from_east(forrest, coordinates, me):
    row, col = coordinates
    line_of_trees = forrest[row, col+1:]
    return is_visible_in_line(line_of_trees, me)


def is_visible_from_south(forrest, coordinates, me):
    row, col = coordinates
    line_of_trees = forrest[row+1:, col]
    return is_visible_in_line(line_of_trees, me)


def is_visible_from_west(forrest, coordinates, me):
    row, col = coordinates
    line_of_trees = forrest[row, :col]
    return is_visible_in_line(line_of_trees, me)


trees = []

for line in input:
    trees.append(list(line.rstrip()))

forrest = np.array(trees)

it = np.nditer(forrest, flags=['multi_index'])
visible_trees = 0
for x in it:
    if is_visible(forrest, x, it.multi_index):
        visible_trees += 1

print(visible_trees)
