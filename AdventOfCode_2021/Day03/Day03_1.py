from typing import Counter
from utils.utils import get_decimal, get_strings, rotate_list


input = get_strings("Day03/input_1.txt")


split = []
for number in input:
    split.append(list(number))

bits = rotate_list(split)

gamma, epsilon = '', ''
for bit in bits:
    most_common = Counter(bit).most_common(1)
    if most_common[0][0] == '1':
        gamma += str(1)
        epsilon += str(0)
    else:
        gamma += str(0)
        epsilon += str(1)

gamma_dec = get_decimal(gamma)
epsilon_dec = get_decimal(epsilon)

print('Day03_1: ', gamma_dec*epsilon_dec)
