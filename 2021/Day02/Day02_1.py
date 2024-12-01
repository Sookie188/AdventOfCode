from utils.utils import get_strings, split_two


input = get_strings("Day02/input_1.txt")
commands = split_two(input)

position, depth = 0, 0
for entry in commands:
    command = entry[0]
    units = int(entry[1])
    if command == 'forward':
        position += units
    elif command == 'down':
        depth += units
    elif command == 'up':
        depth -= units

print("Day02_1: ", position*depth)
