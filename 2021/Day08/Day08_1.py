from utils.utils import get_strings


def get_output(signals):
    output = []
    for i in range(len(signals)):
        signal = signals[i][1]
        output.append(signal.split())
    return output


def get_easy_numbers(output):
    easy_digits = 0
    for digits in output:
        for digit in digits:
            if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
                easy_digits += 1
    return easy_digits


def main():
    input = get_strings("Day08/input_1.txt")

    signals = []
    for line in input:
        signals.append(line.split('|'))

    output = get_output(signals)
    numbers = get_easy_numbers(output)

    print('Day08_1: ', numbers)


if __name__ == '__main__':
    main()
