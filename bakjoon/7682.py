result = []
checks = [[0,1,2], [3,4,5], [6,7,8], [0,4,8], [2,4,6], [0,3,6], [1,4,7], [2,5,8]]

def flag(board,equ):
    for check in checks:
        if board[check[0]] == board[check[1]] == board[check[2]] == equ:
            return 1
    return 0

def is_valid(board):
    x_count = 0
    o_count = 0

    for b in board:
        if b == 'X':
            x_count += 1
        elif b == 'O':
            o_count += 1

    if x_count > o_count + 1:
        return 0
    if o_count > x_count:
        return 0
    if x_count == o_count + 1 and flag(board, 'X') and not flag(board, 'O'):
        return 1
    if x_count == o_count and flag(board, 'O') and not flag(board, 'X'):
        return 1
    if o_count + x_count == 9 and not flag(board, 'O'):
        return 1
    return 0


board = list(input()) 
while board[0] != 'e':
    if is_valid(board):
        result.append('valid')
    else:
        result.append('invalid')
    board = list(input()) 
print('\n'.join(result))