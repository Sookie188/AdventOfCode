from utils.utils import get_strings

input = get_strings("Day06/input_1.txt")
fishie_timers = input[0].split(',')


class Fishie:
    def __init__(self, timer):
        self.timer = timer

    def lower_timer(self):
        self.timer -= 1
        if self.timer == -1:
            self.timer = 6
            return Fishie(8)
        return None


def start_new_day(fishies):
    for i in range(len(fishies)):
        new_fishie = fishies[i].lower_timer()
        if new_fishie is not None:
            fishies.append(new_fishie)


def initialise_first_fishies(fishie_timers):
    fishies = []
    for timer in fishie_timers:
        fishies.append(Fishie(int(timer)))
    return fishies


fishies = initialise_first_fishies(fishie_timers)

for i in range(80):
    start_new_day(fishies)

print("Fishies :", len(fishies))
