filename = "Day02/input.txt"

with open(filename, "r") as fp:
    input = fp.readlines()

rounds = []
for line in input:
    rounds.append(line.rstrip().split(" "))

scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3
}


def pleh(elf, me):
    elf_score = scores[elf]
    # lose
    if me == "X":
        return count_score(elf, 'lose')
    # draw
    elif me == "Y":
        return elf_score + 3
    # win
    elif me == "Z":
        return count_score(elf, 'win') + 6


def count_score(elf, res):
    if res == 'win':
        if elf == "A":
            return 2
        elif elf == "B":
            return 3
        elif elf == "C":
            return 1
    else:
        if elf == "A":
            return 3
        elif elf == "B":
            return 1
        elif elf == "C":
            return 2


final_score = 0
for line in rounds:
    final_score += pleh(line[0], line[1])

print(final_score)
