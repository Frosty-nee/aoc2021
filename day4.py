#! python

import utils

def process_input(i):
    draws = list(map(int, i[0].split(',')))
    boards = []
    board = []
    for count, line in enumerate(i[2:]):
        if count == len(i[2:])-1:
            boards.append(board)
        if len(line) > 0:
            board.append(list(map(int, line.split())))
        else:
            boards.append(board)
            board = []
    for board in boards:
        for line in board:
            for pos, number in enumerate(line):
               line[pos] = (False, number)
    return draws, boards

def check_win(boards):
    def check_columns(board):
        for column in range(len(board[0])):
            win = True
            for line in board:
                if not line[column][0]:
                    win = False
                    continue
            if win:
                return True

    def check_rows(board):
        for row in range(len(board[0])):
            win = True
            for rowpos, num in enumerate(board[row]):
                if not num[0]:
                    win = False
            if win:
                return True
    winners = []
    for board in boards:
        if check_columns(board) or check_rows(board):
            winners.append(board)
    return winners

def calculate_score(board, draw):
    score = 0
    for line in board:
        for col in line:
            if not col[0]:
                score += col[1]
    return score*draw

def solve(draws, boards):
    winners = []
    for draw in draws:
        for board in boards:
            for row in board:
                for col, num in enumerate(row):
                    if num[1] == draw:
                        row[col] = (True, num[1])
        if b := check_win(boards):
            for wb in b:
                winners.append((wb, draw))
                boards.remove(wb)
            if len(boards) == 0:
                break
        if len(boards) == 0:
            break
    return winners

if __name__ == '__main__':
    draws, boards = process_input(utils.process_raw_input('i4'))
    winners = solve(draws, boards)
    print(calculate_score(winners[0][0], winners[0][1]))
    print(calculate_score(winners[-1][0], winners[-1][1]))