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
    me_score = scores[me]
    if me == "X" and elf == "C":
        return me_score + 6
    elif me == "Y" and elf == "A":
        return me_score + 6
    elif me == "Z" and elf == "B":
        return me_score + 6
    elif scores[me] == scores[elf]:
        return me_score + 3
    else:
        return me_score


final_score = 0
for line in rounds:
    final_score += pleh(line[0], line[1])

print(final_score)
