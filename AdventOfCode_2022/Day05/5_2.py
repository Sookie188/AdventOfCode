with open("Day05/input.txt", "r") as fp:
    input = fp.readlines()


def parse_instructions(line):
    split_line = line.rstrip().split(' ')
    return (int(split_line[1]), int(split_line[3])-1, int(split_line[5])-1)


stacks = []
instructions = []
for line in input:
    if 'move' not in line:
        stacks.append(line.rstrip().split(','))
    else:
        instructions.append(parse_instructions(line))


def move_all_elems(source, target, num_of_elems):
    target.extend(source[-num_of_elems:])
    for _ in range(num_of_elems):
        source.pop()


def get_result(stacks):
    result = []
    for stack in stacks:
        if len(stack) >= 1:
            result.append(stack[-1])
    return ''.join(result)


for instruction in instructions:
    times, source, target = instruction
    move_all_elems(stacks[source], stacks[target], times)

print(get_result(stacks))
