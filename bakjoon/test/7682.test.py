from itertools import count
import sys
from copy import deepcopy

input = sys.stdin.readline
result = []
checks = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8]]

def is_valid(board):
    
    x_count = 0
    o_count = 0

    for b in board:
        if b == 'X':
            x_count += 1
        elif b == 'O':
            o_count += 1
        elif b == '.':
            continue
        else:
            return 0
    if not(x_count == o_count + 1 or o_count == x_count):
        return 0
    if len(board) > 9 or len(board) < 9:
        return 0
    x_win = 0
    o_win = 0
    for check in checks:
        start = board[check[0]]
        end_check = 1
        if start == '.':
            continue
        for nxt in check[1:]:
            if start == board[nxt]:
                continue
            end_check = 0
            break
        if not end_check:
            continue
        if start == 'X':
            x_win += 1
        else:
            o_win += 1
    
    if x_win > 0 and o_win > 0:
        return 0
    elif x_win > 0 and x_count == o_count + 1:
        return 1
    elif o_win > 0 and x_count == o_count:
        return 1
    elif o_count + x_count == 9:
        return 1
    return 0

def main(board):
    if is_valid(board):
        return "valid"
    else:
        return "invalid"

def soultion(line):
    game_list = [[0] * 3 for _ in range(3)]
    # line = input()
    num_X = 0
    num_O = 0
    for i in range(3):
        for j in range(3):
            game_list[i][j] = line[i * 3 + j]
            if game_list[i][j] == 'O':
                num_O += 1
            elif game_list[i][j] == 'X':
                num_X += 1

    # 문제 조건상 X 가 먼저 이므로 무조건 X의 갯수가 O보다 많아야하고,
    # 번갈아 가며 플레이 하므로 둘의 차이가 1 또는 0 이어야 함
    if num_X - num_O != 0 and num_X - num_O != 1:
        return "invalid"

    score = ['.'] * 8
    for i in range(3):
        if game_list[i][0] == game_list[i][1] and game_list[i][1] == game_list[i][2]:
            score[i] = game_list[i][0]
        if game_list[0][i] == game_list[1][i] and game_list[1][i] == game_list[2][i]:
            score[3 + i] = game_list[0][i]
    if game_list[0][0] == game_list[1][1] and game_list[1][1] == game_list[2][2]:
        score[6] = game_list[1][1]
    if game_list[0][2] == game_list[1][1] and game_list[1][1] == game_list[2][0]:
        score[7] = game_list[1][1]

    success_X = score.count('X')
    success_O = score.count('O')
    # print(index, score)
    # 성공 갯수 0개 > 게임판이 가득 찬 경우
    if success_X + success_O == 0:
        if num_X + num_O == 9:
            return "valid"
        else:
            return "invalid"
    # 성공 갯수 1개
    elif success_X + success_O == 1:
        # O 가 이긴 경우
        if num_X - num_O == 0:
            if success_O == 1:
                return "valid"
        # X 가 이긴 경우
        elif num_X - num_O == 1:
            if success_X == 1:
                return "valid"
        return "invalid"
    # 성공 갯수 2개 이상
    # 성공이 모두 동일한 사람이어야 하며, 마지막 하나의 칸으로 여러개가 성공이 될 수 있어야함
    # 해당 상황에서는 X만 가능하다.
    else:
        if success_X > 0 and success_O > 0:
            return "invalid"
        # X 가 이긴 경우
        elif success_X > 0:
            if num_X - num_O == 1:
                return "valid"
            return "invalid"
        # O 가 이긴 경우 > 이런 경우는 없다
        else:
            return "invalid"


board = ['.'] * 9
index = 0
counting =0 
def DFS(board, index):
    global counting 
    counting += 1
    if index >= 9:
        return None

    # print(main(board), soultion(board))
    if main(board) != soultion(board):
        print(main(board), soultion(board))
        result.append(board)
        return 'end'

    new_board = deepcopy(board)
    print(new_board, index)
    DFS(new_board, index + 1)
    new_board[index] = 'X'
    print(new_board, index)
    DFS(new_board, index + 1)
    new_board[index] = 'O'
    print(new_board, index)
    DFS(new_board, index + 1)
    return 'end'

DFS(board, 0)
print(result, counting)