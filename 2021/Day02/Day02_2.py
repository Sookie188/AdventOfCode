from utils.utils import get_strings, split_two


input = get_strings('Day02/input_1.txt')
commands = split_two(input)

position, depth, aim = 0, 0, 0
for entry in commands:
    command = entry[0]
    units = int(entry[1])
    if command == 'forward':
        position += units
        depth += aim*units
    elif command == 'down':
        aim += units
    elif command == 'up':
        aim -= units

print('Day02_2: ', position*depth)
