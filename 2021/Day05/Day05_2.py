
from Day05.Day05_1 import count_overlaps, create_field, get_max_x, get_max_y
from utils.utils import get_strings


def draw_fancy_line(field, line):
    for point in get_line(line[0], line[1]):
        field[point[0]][point[1]] += 1

# this was not written by me, I'm not that smart :)
# https://newbedev.com/python-bresenhams-line-drawing-algorithm-python-code-example


def get_line(start, end):
    """Bresenham's Line Algorithm
    Produces a list of tuples from start and end

    >>> points1 = get_line((0, 0), (3, 4))
    >>> points2 = get_line((3, 4), (0, 0))
    >>> assert(set(points1) == set(points2))
    >>> print points1
    [(0, 0), (1, 1), (1, 2), (2, 3), (3, 4)]
    >>> print points2
    [(3, 4), (2, 3), (1, 2), (1, 1), (0, 0)]
    """
    # Setup initial conditions
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1

    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)

    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1

    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1

    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    return points


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

    field = create_field(get_max_x(lines) + 1,
                         get_max_y(lines) + 1)

    for line in lines:
        draw_fancy_line(field, line)

    print('Day05_2: ', str(count_overlaps(field)))


if __name__ == '__main__':
    main()
