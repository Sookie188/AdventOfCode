from utils.utils import get_strings
from collections import deque


def get_strings(filename):
    with open(filename, "r") as fp:
        num = fp.readlines()
    return [str(i.rstrip()) for i in num]


def start_new_day(fishies):
    buffer = fishies.popleft()
    fishies[6] += buffer
    fishies.append(buffer)


def initialise_first_fishies(fishie_timers):
    fishies = []
    fishies.append(0)
    fishies.append(sum(p == '1' for p in fishie_timers))
    fishies.append(sum(p == '2' for p in fishie_timers))
    fishies.append(sum(p == '3' for p in fishie_timers))
    fishies.append(sum(p == '4' for p in fishie_timers))
    fishies.append(sum(p == '5' for p in fishie_timers))
    fishies.append(0)
    fishies.append(0)
    fishies.append(0)

    fishies = deque(fishies)
    return fishies


input = get_strings("Day06/input_1.txt")
fishie_timers = input[0].split(',')

fishies = initialise_first_fishies(fishie_timers)

for i in range(0, 256):
    start_new_day(fishies)

amount = 0
for i in range(0, len(fishies)):
    amount = amount + fishies[i]

print("Fishies :", amount)
