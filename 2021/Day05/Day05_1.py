
from utils.utils import get_strings


def is_hor_or_vert(line):
    start, end = line
    if start[0] == end[0] or start[1] == end[1]:
        return True
    return False


def get_max_x(lines):
    x = []
    for line in lines:
        x.append(line[0][0])
        x.append(line[1][0])
    return max(x)


def get_max_y(lines):
    y = []
    for line in lines:
        y.append(line[0][1])
        y.append(line[1][1])
    return max(y)


def create_field(x, y):
    field = []
    for i in range(x):
        line = []
        for j in range(y):
            line.append(0)
        field.append(line)
    return field


def draw_field(field):
    for row in field:
        print(''.join(map(str, row)))


def get_hor_lines(start, end):
    points = []
    for i in range(min([start[1], end[1]]), max([start[1], end[1]])+1):
        points.append([start[0], i])
    return points


def get_vert_lines(start, end):
    points = []
    for i in range(min([start[0], end[0]]), max([start[0], end[0]])+1):
        points.append([i, start[1]])
    return points


def get_line_points(start, end):
    if start[0] == end[0]:
        return get_hor_lines(start, end)
    elif start[1] == end[1]:
        return get_vert_lines(start, end)


def draw_line(field, line):
    for point in get_line_points(line[0], line[1]):
        field[point[0]][point[1]] += 1


def count_overlaps(field):
    counter = 0
    for row in field:
        for col in row:
            if col >= 2:
                counter += 1
    return counter


def main():
    input = get_strings("Day05/input_1.txt")

    lines = []
    for line in input:
        start, end = line.split(' -> ')
        start_x, start_y = start.split(',')
        start_x = int(start_x)
        start_y = int(start_y)
        end_x, end_y = end.split(',')
        end_x = int(end_x)
        end_y = int(end_y)
        lines.append([[start_x, start_y], [end_x, end_y]])

    filtered_lines = []
    for line in lines:
        if is_hor_or_vert(line):
            filtered_lines.append(line)

    field = create_field(get_max_x(filtered_lines) + 1,
                         get_max_y(filtered_lines) + 1)

    for line in filtered_lines:
        draw_line(field, line)

    print('Day05_1: ', str(count_overlaps(field)))


if __name__ == '__main__':
    main()
