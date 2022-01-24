import sys
input = sys.stdin.readline

R,C = map(int, input().split())
board = [0] * R

for i in range(R):
    board[i] = list(input().rstrip())
    
N = int(input())
values = list(map(int,input().split()))

for i in range(N):
    # 왼쪽에서 던짐
    cur_row = N - values[i]
    target = []
    if i % 2 == 0:
        for cur_col in range(C):
            if board[cur_row][cur_col] == 'x':
                target = [cur_row, cur_col]
                