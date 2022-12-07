from utils.utils import get_strings


def get_complete_output(signals):
    output = []
    for signal in signals:
        line = []
        for part in signal:
            line.append(part.split())
        output.append(line)
    return output


def sort_input(input):
    sorted_input = []
    for line in input:
        row = []
        for part in line:
            sorted_parts = []
            for string in part:
                sorted_string = "".join(sorted(string))
                sorted_parts.append(sorted_string)
            row.append(sorted_parts)
        sorted_input.append(row)
    return sorted_input


def containsAll(str, set):
    for c in set:
        if c not in str:
            return 0
    return 1


def contains_just_one(str, set):
    counter = 0
    for c in set:
        if c in str:
            counter += 1
    if counter == 1:
        return True
    else:
        return False


def contains_five(str, set):
    counter = 0
    for c in set:
        if c in str:
            counter += 1
    if counter == 5:
        return True
    else:
        return False


def is_zero(signal, one, nine):
    return len(signal) == 6 and containsAll(signal, one) and not nine


def is_one(signal):
    return len(signal) == 2


def is_three(signal, seven):
    return len(signal) == 5 and containsAll(signal, seven)


def is_four(signal):
    return len(signal) == 4


def is_five(signal, six):
    return len(signal) == 5 and contains_five(signal, six)


def is_six(signal, one):
    return len(signal) == 6 and contains_just_one(signal, one)


def is_seven(signal):
    return len(signal) == 3


def is_eight(signal):
    return len(signal) == 7


def is_nine(signal, three):
    if len(signal) == 6 and containsAll(signal, three):
        return True
    return False


def mapping(line):
    result = [None]*10
    signals = list(sorted(line[0], key=len))
    for signal in signals:
        if is_one(signal):
            result[1] = signal
        if is_four(signal):
            result[4] = signal
        if is_seven(signal):
            result[7] = signal
        if is_eight(signal):
            result[8] = signal
        if is_three(signal, result[7]):
            result[3] = signal
        if is_nine(signal, result[3]):
            result[9] = signal
        if is_zero(signal, result[1], is_nine(signal, result[3])):
            result[0] = signal
        if is_six(signal, result[1]):
            result[6] = signal

    for signal in signals:
        if len(signal) == 5 and not is_three(signal, result[7]):
            if is_five(signal, result[6]):
                result[5] = signal
            else:
                result[2] = signal
    return result


def get_numbers(line, mapping):
    outputs = line[1]
    value = []
    number_output = []
    for output in outputs:
        for number in mapping:
            if len(output) == len(number) and containsAll(output, number):
                number_output.append(str(mapping.index(number)))
    number = ("".join(number_output))
    return number


def main():
    input = get_strings("Day08/input_1.txt")

    signals = []
    for line in input:
        signals.append(line.split('|'))

    output = get_complete_output(signals)

    value = 0
    for line in output:
        mapping_final = mapping(line)
        value += int(get_numbers(line, mapping_final))

    print('Day08_2: ', value)


if __name__ == '__main__':
    main()
