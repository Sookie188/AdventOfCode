from utils.utils import get_strings
from Day04_1 import read_boards, update_boards, get_winners, calculate_score


def main():
    input = get_strings("Day04/input_1.txt")
    numbers = input[0].split(',')
    boards = read_boards(input[2:])

    for number in numbers:
        update_boards(boards, number)
        winners = get_winners(boards)
        if len(boards) == len(winners):
            print('Day04_2: ', calculate_score(winners[0], number))
            break
        for winner in winners:
            boards.remove(winner)


if __name__ == '__main__':
    main()
