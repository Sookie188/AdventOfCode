from os import set_blocking
from utils.utils import get_strings


def align_crabs(positions, point):
    fuel = 0
    for i in range(len(positions)):
        pos = positions[i]
        if point > pos:
            steps = point - pos
            for i in range(steps+1):
                fuel += i
        else:
            steps = pos - point
            for i in range(steps+1):
                fuel += i
    return fuel


def check_cheapest_way(positions, first_fuel):
    for i in range(min(positions), max(positions)):
        fuel_needed = align_crabs(positions, i)
        if fuel_needed < first_fuel:
            first_fuel = fuel_needed
        print(i)
    return first_fuel


input = get_strings("Day07/input_1.txt")
split = input[0].split(',')
positions = [int(string) for string in split]
first_fuel = align_crabs(positions, 0)

print('Day07_2: ', check_cheapest_way(positions, first_fuel))
