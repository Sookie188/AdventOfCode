from utils.utils import get_numbers, get_strings


def read_boards(input_lines):
    boards = []
    current = []
    for line in input_lines:
        if len(line) == 0:
            boards.append(current)
            current = []
        else:
            current.append(line.split())
    boards.append(current)
    return boards


def update_board(board, number):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == number:
                board[row][col] = 'X'


def update_boards(boards, number):
    for board in boards:
        update_board(board, number)


def check_rows(board):
    for row in board:
        col_bools = []
        for col in row:
            col_bools.append(col == 'X')
        if all(col_bools):
            return True
    return False


def check_columns(board):
    for col in range(len(board)):
        row_bools = []
        for row in range(len(board)):
            row_bools.append(board[row][col] == 'X')
        if all(row_bools):
            return True
    return False


def check_win(board):
    return check_rows(board) or check_columns(board)


def get_winners(boards):
    winners = []
    for board in boards:
        if check_win(board):
            winners.append(board)
    return winners


def calculate_score(board, number):
    score = 0
    for row in board:
        for col in row:
            if col != 'X':
                score += int(col)
    return score*int(number)


def main():
    input = get_strings("Day04/input_1.txt")
    numbers = input[0].split(',')
    boards = read_boards(input[2:])

    for number in numbers:
        update_boards(boards, number)
        winners = get_winners(boards)
        if len(winners) > 0:
            print('Day04_1: ', calculate_score(winners[0], number))
            break


if __name__ == '__main__':
    main()
