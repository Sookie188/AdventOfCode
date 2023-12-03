with open("AdventOfCode_2023/input/02.txt") as fp:
    input = fp.readlines()

def part1(input):
    maxRed = 12
    maxGreen = 13
    maxBlue = 14
    possible = 0
    impossibleGames = set()
    for line in input:
        game, bag = line.split(":")
        splitGame = game.split()
        gameID = int(splitGame[1])
        possible += gameID
        reveals = bag.split(";")
        for reveal in reveals:
            cubes = reveal.split(",")
            for cube in cubes:
                num, color = cube.split()
                color = color.strip()
                num = int(num)
                if color == 'red' and num > maxRed:
                    impossibleGames.add(gameID)
                    break
                if color == 'green' and num > maxGreen:
                    impossibleGames.add(gameID)
                    break
                if color == 'blue' and num > maxBlue:
                    impossibleGames.add(gameID)
                    break
    sumOfImpossible = sum(list(impossibleGames))  
    result = possible - sumOfImpossible             
    print(result)


def part2(input):
    power = 0 
    powerSum = 0
    for line in input:
        _, bag = line.split(":")
        reveals = bag.split(";")
        maxRed = 0
        maxGreen = 0
        maxBlue = 0
        for reveal in reveals:
            cubes = reveal.split(",")
            for cube in cubes:
                num, color = cube.split()
                color = color.strip()
                num = int(num)
                if color == 'red':
                    if num > maxRed:
                        maxRed = num
                if color == 'green':
                    if num > maxGreen:
                        maxGreen = num
                if color == 'blue':
                    if num > maxBlue:
                        maxBlue = num
        power = maxRed*maxGreen*maxBlue
        powerSum += power
    print(powerSum)

print("Ergebnis Part1: ")
part1(input)

print("Ergebnis Part2: ")
part2(input)
