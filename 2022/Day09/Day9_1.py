with open("AdventOfCode_2022/Day09/input.txt", "r") as fp:
    input = fp.readlines()


def move_head(direction, pos_head):
    if direction == 'R':
        return move_right(pos_head)
    if direction == 'L':
        return move_left(pos_head)
    if direction == 'U':
        return move_up(pos_head)
    if direction == 'D':
        return move_down(pos_head)
    print(direction, ' is no direction')


def is_tail_in_range(pos_head, pos_tail):
    if pos_head == pos_tail:
        return True
    x_head, y_head = pos_head
    x_tail, y_tail = pos_tail
    x_diff = abs(x_head - x_tail)
    y_diff = abs(y_head - y_tail)
    return x_diff <= 1 and y_diff <= 1


def move_right(coordinates):
    x, y = coordinates
    return (x, y+1)


def move_left(coordinates):
    x, y = coordinates
    return (x, y-1)


def move_up(coordinates):
    x, y = coordinates
    return (x+1, y)


def move_down(coordinates):
    x, y = coordinates
    return (x-1, y)


moves = []
for line in input:
    moves.append((line.rstrip().split()))


visited = []
pos_head = (0, 0)
pos_tail = (0, 0)
for move in moves:
    direction, steps = move
    for _ in range(int(steps)):
        pos_head_init = pos_head
        pos_head = move_head(direction, pos_head)
        if not is_tail_in_range(pos_head, pos_tail):
            pos_tail = pos_head_init
        visited.append(pos_tail)


unique_data = set(visited)
print(len(unique_data))
