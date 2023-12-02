with open("AdventOfCode_2023/01.txt") as fp:
    input = fp.readlines()
   
def part1(input):
    values = []
    twoDigits = []
    for line in input:
        values.append(''.join(filter(str.isdigit,line)))

    for value in values:
        digit = str(value[0] + str(value[-1]))
        twoDigits.append(int(digit))
    print(sum(twoDigits))

def wordToDigit(value):
    # thank you random guy on reddit for saving my sanity <3
    # Wir lassen einfach den ersten und letzten Buchstaben von der Zahl stehen, damit wir Überscheidungen behandeln können.
    rules = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}

    for word, digit in rules.items():
        value = value.replace(word, digit)

    return value

def part2(input):
    justNumbers = []
    for value in input:
        result = wordToDigit(value)
        justNumbers.append((result.strip()))
    part1(justNumbers)



print("Ergebnis Part1: ")
part1(input)

print("Ergebnis Part2: ")
part2(input)
