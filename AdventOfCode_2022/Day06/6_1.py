with open("AdventOfCode_2022/Day06/input.txt", "r") as fp:
    input = fp.read()


def is_unique(mystr):
    return len(mystr) == len(set(mystr))


def check_marker(windowsize, input):
    for i in range(len(input)-windowsize):
        if is_unique(input[i:i+windowsize]):
            return (i+windowsize)


# part 1
print(check_marker(4, input))

# part 2
print(check_marker(14, input))
