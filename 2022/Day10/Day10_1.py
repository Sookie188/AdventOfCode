with open("AdventOfCode_2022/Day10/input.txt", "r") as fp:
    input = fp.readlines()

instructions = []
for line in input:
    instructions.append((line.rstrip().split()))


def check_ticks(tick, x):
    if tick == 20:
        return tick*x
    elif tick == 60:
        return tick*x
    elif tick == 100:
        return tick*x
    elif tick == 140:
        return tick*x
    elif tick == 180:
        return tick*x
    elif tick == 220:
        return tick*x
    else:
        return 0


x = 1
tick = 1
signal_strengths = 0
for i in range(len(instructions)):
    instruction = instructions[i]
    if instruction[0] == 'noop':
        tick += 1
        signal_strengths += check_ticks(tick, x)
    elif instruction[0] == 'addx':
        tick += 1
        signal_strengths += check_ticks(tick, x)
        x = x+int(instruction[1])
        tick += 1
        signal_strengths += check_ticks(tick, x)

print(signal_strengths)
