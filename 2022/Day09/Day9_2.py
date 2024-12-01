with open("AdventOfCode_2022/Day09/input.txt", "r") as fp:
    input = fp.readlines()


class Knot:
    def __init__(self, pos_x, pos_y):
        self.pos = (pos_x, pos_y)
        self.next = None

    def __str__(self):
        return str(self.pos) + (' -> ' + str(self.next) if self.next is not None else '')

    def move(self, new_pos):
        self.pos = new_pos


def init_snek(knots):
    head = Knot(0, 0)
    current = head
    for _ in range(knots-1):
        current.next = Knot(0, 0)
        current = current.next
    return head, current


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
    return (x+1, y)


def move_left(coordinates):
    x, y = coordinates
    return (x-1, y)


def move_up(coordinates):
    x, y = coordinates
    return (x, y+1)


def move_down(coordinates):
    x, y = coordinates
    return (x, y-1)


def move_diagonal(head, tail):
    if head[0] < tail[0]:
        intermediate = move_left(tail)
    else:
        intermediate = move_right(tail)
    if head[1] < tail[1]:
        intermediate = move_down(intermediate)
    else:
        intermediate = move_up(intermediate)
    return intermediate


def move_horizontal(head, tail):
    if head[0] < tail[0]:
        return move_left(tail)
    return move_right(tail)


def move_vertical(head, tail):
    if head[1] < tail[1]:
        return move_down(tail)
    return move_up(tail)


def pull_tail(knot):
    tail = knot.next
    if not is_tail_in_range(knot.pos, tail.pos):
        if knot.pos[0] == tail.pos[0]:
            # we are in the same col
            tail.move(move_vertical(knot.pos, tail.pos))
        elif knot.pos[1] == tail.pos[1]:
            # we are in the same row
            tail.move(move_horizontal(knot.pos, tail.pos))
        else:
            # we have to move diagonal
            tail.move(move_diagonal(knot.pos, tail.pos))


def pull_tails(head):
    current = head
    while current.next is not None:
        pull_tail(current)
        current = current.next


moves = []
for line in input:
    moves.append((line.rstrip().split()))


snek_head, snek_tail = init_snek(10)


visited = set()
for move in moves:
    direction, steps = move
    for _ in range(int(steps)):
        new_head_pos = move_head(direction, snek_head.pos)
        snek_head.move(new_head_pos)
        pull_tails(snek_head)
        visited.add(snek_tail.pos)

print(len(visited))
