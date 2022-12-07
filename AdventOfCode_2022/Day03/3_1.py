with open("Day03/input.txt", "r") as fp:
    input = fp.readlines()


def check_compartments(first_comp, second_comp):
    for item in first_comp:
        if (item in second_comp):
            return get_priority(item)
            break


def get_priority(item):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96


rucksacks = []
result = 0
for line in input:
    length = int(len(line.rstrip()) / 2)
    first_comp = line[:length]
    second_comp = line[length:]
    result += check_compartments(first_comp, second_comp)

print(result)
