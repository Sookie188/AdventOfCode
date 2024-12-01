import numpy as np

with open("AdventOfCode_2022/Day12/input.txt", "r") as fp:
    input = fp.readlines()

heights = []
for line in input:
    heights.append([[height, 99999999999] for height in list(line.rstrip())])

heightmap = np.array(heights)
end_raw = np.where(heightmap == 'E')

more_starts = []
start_raw_2 = np.nonzero(heightmap == 'a')
listOfFucksIGive = list(zip(start_raw_2[0], start_raw_2[1]))
for fuck in listOfFucksIGive:
    more_starts.append(fuck)

end = (end_raw[0][0], end_raw[1][0])


def move_is_valid(new_pos, current_pos, check_heightmap):
    x, y, _ = check_heightmap.shape
    if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= x or new_pos[1] >= y:
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
        return False
    if current_height - check_height >= -1:
        return True
    return False


def find_shortest_path(heightmap, start):
    neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    check_heightmap = heightmap
    paths_to_check = [start]

    while paths_to_check:
        current_pos = paths_to_check.pop(0)
        current_distance = int(check_heightmap[current_pos][1])+1
        for neighbour in neighbours:
            new_pos = (current_pos[0] + neighbour[0],
                       current_pos[1] + neighbour[1])
            if not move_is_valid(new_pos, current_pos, check_heightmap):
                continue
            paths_to_check.append(new_pos)
            check_heightmap[new_pos][1] = current_distance


result_list = []
for start in more_starts:
    heightmap[start][1] = 0
    find_shortest_path(heightmap, start)
    result = heightmap[end][1]
    if result not in result_list:
        result_list.append(result)


print(min(result_list))
print(end) 
