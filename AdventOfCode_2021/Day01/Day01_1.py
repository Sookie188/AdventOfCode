from utils.utils import get_numbers


input = get_numbers("Day01/input_1.txt")

increases = 0
for i in range(1, len(input)):
    if (input[i] > input[i-1]):
        increases += 1

print("Day01_1: ", increases)
