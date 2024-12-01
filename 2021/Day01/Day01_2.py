from utils.utils import get_numbers


input = get_numbers("Day01/input_1.txt")

increases = 0
for i in range(2, len(input)-1):
    firstWindow = input[i] + input[i-1] + input[i-2]
    secondWindow = input[i+1] + input[i] + input[i-1]
    if secondWindow > firstWindow:
        increases += 1

print("Day01_2: ", increases)
