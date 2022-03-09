import sys
input = sys.stdin.readline

result = []
checks = [[0,1,2], [3,4,5], [6,7,8], [0,4,8], [2,4,6], [0,3,6], [1,4,7], [2,5,8]]
exception_case = ['X','O','X','O','X','O','X','O','X']

def is_valid(board):
    x_count = 0
    o_count = 0

    for b in board:
        if b == 'X':
            x_count += 1
        elif b == 'O':
            o_count += 1
    if x_count > 5 or o_count > 4:
        return 0
    if not(x_count == o_count + 1 or o_count == x_count):
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
    if o_count + x_count == 9:
        return 1
    return 0


board = list(input().rstrip()) 
while board[0] != 'e':
    if is_valid(board):
        result.append('valid')
    else:
        result.append('invalid')
    board = list(input().rstrip()) 
print('\n'.join(result))