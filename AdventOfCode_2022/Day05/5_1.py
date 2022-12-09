with open("AdventOfCode_2022/Day05/input.txt", "r") as fp:
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


def move_elem(source, target):
    target.append(source.pop())


def get_result(stacks):
    result = []
    for stack in stacks:
        if len(stack) >= 1:
            result.append(stack[-1])
    return ''.join(result)


for instruction in instructions:
    times, source, target = instruction
    for _ in range(times):
        move_elem(stacks[source], stacks[target])

print(get_result(stacks))
