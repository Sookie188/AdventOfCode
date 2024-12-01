with open("AdventOfCode_2022/Day10/input.txt", "r") as fp:
    input = fp.readlines()

instructions = []
for line in input:
    instructions.append((line.rstrip().split()))


def draw_screen(crt, sprite_pos):
    crt_pos = len(crt) % 40
    if sprite_pos - 1 <= crt_pos <= sprite_pos + 1:
        return '#'
    else:
        return '.'


def print_screen(crt):
    for i in range(0, len(crt), 40):
        print(''.join(crt[i:i+40]))


x = 1
tick = 1
signal_strengths = 0
crt = []
for i in range(len(instructions)):
    instruction = instructions[i]
    if instruction[0] == 'noop':
        tick += 1
        crt.append(draw_screen(crt, x))
    elif instruction[0] == 'addx':
        tick += 1
        crt.append(draw_screen(crt, x))
        crt.append(draw_screen(crt, x))
        x = x+int(instruction[1])
        tick += 1

print_screen(crt)
