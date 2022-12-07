with open("Day03/input.txt", "r") as fp:
    input = fp.readlines()


def check_rucksack(first, second, third):
    for item in first:
        if (item in second and item in third):
            return get_priority(item)
            break


def get_priority(item):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96


rucksacks = []
result = 0
for i in range(0, len(input), 3):
    result += check_rucksack(input[i], input[i+1], input[i+2])

print(result)
