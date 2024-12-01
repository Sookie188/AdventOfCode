from utils.utils import get_strings


def align_crabs(positions, point):
    fuel = 0
    for i in range(len(positions)):
        pos = positions[i]
        if point > pos:
            fuel += point - pos
        else:
            fuel += pos - point
    return fuel


input = get_strings("Day07/input_1.txt")
split = input[0].split(',')
positions = [int(string) for string in split]
first_fuel = align_crabs(positions, 0)

for i in range(1, max(positions)):
    fuel_needed = align_crabs(positions, i)
    if fuel_needed < first_fuel:
        first_fuel = fuel_needed

print('Day07_1: ', first_fuel)
