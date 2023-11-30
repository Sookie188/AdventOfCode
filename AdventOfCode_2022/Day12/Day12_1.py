import numpy as np
import math

with open("AdventOfCode_2022/Day12/input.txt", "r") as fp:
    input = fp.readlines()

heights = [] 

for line in input:
    heights.append([[height, 99999999999] for height in list(line.rstrip())])

heightmap = np.array(heights)

start_raw = np.where(heightmap == 'S')
end_raw = np.where(heightmap == 'E')

start = (start_raw[0][0], start_raw[1][0])
heightmap[start][1] = 0
end = (end_raw[0][0], end_raw[1][0])


def move_is_valid(new_pos, current_pos, check_heightmap):
    x, y, _ = check_heightmap.shape
    if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= x or new_pos[1] >= y:
        print('>>> outside grid <<<')
        return False
    current_height = ord(check_heightmap[current_pos][0])
    if check_heightmap[current_pos][0] == 'S':
        current_height = ord('a')
    if check_heightmap[new_pos][0] == 'E':
        check_height = ord('z')
    else:
        check_height = ord(check_heightmap[new_pos][0])
    current_distance = int(check_heightmap[current_pos][1]) + 1
    new_distance = int(check_heightmap[new_pos][1])
    if new_distance <= current_distance:
        print('y u no move', new_distance, current_distance)
        return False
    if current_height - check_height >= -1:
        print('y u move', current_height, check_height)
        return True

    print('y u no move', current_height, check_height,
          new_distance, current_distance)
    return False


def find_shortest_path(heightmap, start):
    neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    check_heightmap = heightmap
    paths_to_check = [start]

    while paths_to_check:
        # print('check: ', paths_to_check[0])
        current_pos = paths_to_check.pop(0)
        print('cur pos: ', current_pos)
        current_height = check_heightmap[current_pos][0]
        # print('cur height: ', current_height)
        current_distance = int(check_heightmap[current_pos][1])+1
        print('cur dist: ', current_distance)

        print('%%%%%%%% check neighbours for', current_pos, '%%%%%%%%%%')
        for neighbour in neighbours:
            new_pos = (current_pos[0] + neighbour[0],
                       current_pos[1] + neighbour[1])
            print('check neighbour: ', new_pos)
            if not move_is_valid(new_pos, current_pos, check_heightmap):
                print('move to ', new_pos, ' is not valid')
                continue
            print('new distance: ', current_distance)
            paths_to_check.append(new_pos)
            print('#### add ', new_pos, ' to List')
            check_heightmap[new_pos][1] = current_distance


find_shortest_path(heightmap, start)
print(heightmap[end])
print(theEnd)
