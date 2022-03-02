
import sys
input = sys.stdin.readline

M,N,H = map(int,input().split())

board = [[list(map(int, input().split())) for i in range(N)] for i in range(H)]

good_tomatos = []
good_and_empty_count = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 1:
                good_tomatos.append((i,j,k))

                good_and_empty_count+=1
            elif board[i][j][k] == -1:
                good_and_empty_count += 1

days = 0

plus_ways = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

def not_valid(h,r,c):
    if h < 0 or h > H - 1:
        return 1
    if r < 0 or r > N - 1:
        return 1
    if c < 0 or c > M - 1:
        return 1
    if board[h][r][c] == 0:
        return 0
    return 1
def nxt_tomato(h,r,c, nxt_good_tomatos):
    if not_valid(h,r,c):
        return 0 
    board[h][r][c] = 1
    nxt_good_tomatos.append((h,r,c))
    return 1
while good_tomatos:
    nxt_good_tomatos = []
    for h,r,c in good_tomatos:
        for h_plus, r_plus, c_plus in plus_ways:
            good_and_empty_count += nxt_tomato(h+h_plus, r + r_plus, c + c_plus, nxt_good_tomatos)
    days += 1
    good_tomatos = nxt_good_tomatos
if good_and_empty_count == N * M * H:
    print(days - 1)
else:
    print(-1)