import numpy as np

with open("AdventOfCode_2022/Day08/input.txt", "r") as fp:
    input = fp.readlines()


def get_scenic_score(forrest, tree, coordinates):
    scenic_score = 1
    scenic_score *= viewing_distance_from_north(forrest, coordinates, tree)
    scenic_score *= viewing_distance_from_east(forrest, coordinates, tree)
    scenic_score *= viewing_distance_from_south(forrest, coordinates, tree)
    scenic_score *= viewing_distance_from_west(forrest, coordinates, tree)
    return scenic_score


def get_score_by_line(line_of_trees, me):
    result = 0
    for tree in line_of_trees:
        if tree < me:
            result += 1
        else:
            return result + 1
    return result


def viewing_distance_from_north(forrest, coordinates, me):
    row, col = coordinates
    line_of_trees = forrest[:row, col]
    return get_score_by_line(reversed(line_of_trees), me)


def viewing_distance_from_east(forrest, coordinates, me):
    row, col = coordinates
    line_of_trees = forrest[row, col+1:]
    return get_score_by_line(line_of_trees, me)


def viewing_distance_from_south(forrest, coordinates, me):
    row, col = coordinates
    line_of_trees = forrest[row+1:, col]
    return get_score_by_line(line_of_trees, me)


def viewing_distance_from_west(forrest, coordinates, me):
    row, col = coordinates
    line_of_trees = forrest[row, :col]
    return get_score_by_line(reversed(line_of_trees), me)


trees = []

for line in input:
    trees.append(list(line.rstrip()))

forrest = np.array(trees)

it = np.nditer(forrest, flags=['multi_index'])
scenic_score = 0
for x in it:
    if get_scenic_score(forrest, x, it.multi_index) > scenic_score:
        scenic_score = get_scenic_score(forrest, x, it.multi_index)

print(scenic_score)
