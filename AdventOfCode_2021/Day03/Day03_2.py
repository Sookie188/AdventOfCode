from typing import Counter
from utils.utils import get_decimal, get_strings, rotate_list


input = get_strings("Day03/input_1.txt")


def get_most_common_bits(i, bits):
    most_common = Counter(bits[i]).most_common(2)
    most_common_bit, num_of_most_bits = most_common[0][0], most_common[0][1]
    return most_common_bit, num_of_most_bits


def get_least_common_bits(i, bits):
    most_common = Counter(bits[i]).most_common(2)
    least_common_bit, num_of_least_bits = most_common[1][0], most_common[1][1]
    return least_common_bit, num_of_least_bits


def get_elements_to_keep(split, num, index):
    res = []
    for number in split:
        if number[index] == num:
            res.append(number)
    return res


diagnostic_report = []
for number in input:
    diagnostic_report.append(list(number))
bits = rotate_list(diagnostic_report)


def get_oxygen(diagnostic_report, bits):
    for i in range(len(bits)):
        most_common_bit, num_of_most_bits = get_most_common_bits(i, bits)
        _, num_of_least_bits = get_least_common_bits(i, bits)
        if num_of_most_bits == num_of_least_bits:
            diagnostic_report = get_elements_to_keep(diagnostic_report, '1', i)
        else:
            diagnostic_report = get_elements_to_keep(
                diagnostic_report, most_common_bit, i)
        if len(diagnostic_report) == 1:
            oxygen = (get_decimal(''.join(diagnostic_report[0])))
            break
        bits = rotate_list(diagnostic_report)
    return oxygen


def get_co2(diagnostic_report, bits):
    for i in range(len(bits)):
        _, num_of_most_bits = get_most_common_bits(i, bits)
        least_common_bit, num_of_least_bits = get_least_common_bits(
            i, bits)
        if num_of_most_bits == num_of_least_bits:
            diagnostic_report = get_elements_to_keep(diagnostic_report, '0', i)
        else:
            diagnostic_report = get_elements_to_keep(
                diagnostic_report, least_common_bit, i)
        if len(diagnostic_report) == 1:
            co2 = (get_decimal(''.join(diagnostic_report[0])))
            break
        bits = rotate_list(diagnostic_report)
    return co2


oxygen = get_oxygen(diagnostic_report, bits)
co2 = get_co2(diagnostic_report, bits)

print('Day03_2: ', oxygen*co2)
