with open("AdventOfCode_2023/input/04.txt") as fp:
    input = [x.rstrip() for x in fp.readlines()]

def part1(input):
    points = 0
    for line in input:
        _, numbers = line.split(":")
        winning, myNumbers = numbers.split("|")
        winning = winning.split()
        myNumbers = myNumbers.split()
        wins = []
        for win in winning:
            if win in myNumbers:
                wins.append(win)
        if len(wins) >= 1:
            points += 2**(len(wins)-1)
    print("Points:",points)

def part2(input):
    cards = []
    for line in input:
        card, numbers = line.split(":")
        cardNum = int(''.join(char for char in card if char.isdigit()))
        winning, myNumbers = numbers.split("|")
        winning = winning.split()
        myNumbers = myNumbers.split()
        wins = []
        copys = cards.count(cardNum)
        for win in winning:
            if win in myNumbers:
                wins.append(win)

        for i in range(copys+1):
            for i in range(0, len(wins)):
                cards.append(cardNum+(i+1))
        
    print(len(input)+len(cards))

print("Ergebnis Part1: ")
part1(input)

print("Ergebnis Part2: ")
part2(input)
