import numpy as np

with open("AdventOfCode_2023/input/03.txt") as fp:
    input = [x.rstrip() for x in fp.readlines()]


def checkRow(row, start, end):
    numbers = []
    s_col = start
    while s_col <= end:
        if row[s_col].isdigit():
            # found number
            # find left boundary of number
            left = s_col
            while left >= 0 and row[left].isdigit():
                left -= 1
            left += 1
            # find right boundary of number
            right = s_col
            while right < row.shape[0] and row[right].isdigit():
                right += 1
            right -= 1

            numbers.append(
                int(''.join(row[left:right+1])))

            s_col = right + 1
        else:
            # no number found -> business as usual
            s_col += 1
    return numbers


def part1(input):
    engine = np.array([list(row) for row in input])

    def findPartNumbers():
        partNumbers = []
        for row in range(0, engine.shape[0] - 1):
            for col in range(0, engine.shape[1] - 1):
                if engine[row, col] != '.' and not engine[row, col].isdigit():
                    # current location is special character
                    start_col = col - 1
                    end_col = col + 1
                    # look at row above
                    partNumbers.extend(
                        checkRow(engine[row - 1], start_col, end_col))
                    # look at our row
                    partNumbers.extend(
                        checkRow(engine[row], start_col, end_col))
                    # look at row below
                    partNumbers.extend(
                        checkRow(engine[row + 1], start_col, end_col))
        return partNumbers

    partNumbers = findPartNumbers()
    print(sum(partNumbers))


print("Ergebnis Part1: ")
part1(input)


def part2(input):
    ratios = []
    engine = np.array([list(row) for row in input])
    for row in range(0, engine.shape[0] - 1):
        for col in range(0, engine.shape[1] - 1):
            if engine[row][col] == '*':
                # found gear candidate
                start_col = col - 1
                end_col = col + 1
                gear_parts = []
                # look at row above
                gear_parts.extend(
                    checkRow(engine[row - 1], start_col, end_col))
                # look at our row
                gear_parts.extend(
                    checkRow(engine[row], start_col, end_col))
                # look at row below
                gear_parts.extend(
                    checkRow(engine[row + 1], start_col, end_col))
                if len(gear_parts) == 2:
                    ratio = gear_parts[0] * gear_parts[1]
                    ratios.append(ratio)
    print(sum(ratios))


print("Ergebnis Part2: ")
part2(input)
