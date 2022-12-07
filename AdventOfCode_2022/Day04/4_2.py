with open("Day04/input.txt", "r") as fp:
    input = fp.readlines()

sections = []
for line in input:
    first_elv, second_elv = line.split(',')
    start_first, end_first = first_elv.split('-')
    start_first = int(start_first)
    end_first = int(end_first)
    start_second, end_second = second_elv.split('-')
    start_second = int(start_second)
    end_second = int(end_second)
    sections.append([[start_first, end_first], [start_second, end_second]])


def partly_contains(section):
    start_elv1 = section[0][0]
    end_elv1 = section[0][1]
    start_elv2 = section[1][0]
    end_elv2 = section[1][1]
    return end_elv1 < start_elv2 or end_elv2 < start_elv1


result = 0
for i in range(len(sections)):
    if not partly_contains(sections[i]):
        result += 1

print(result)
