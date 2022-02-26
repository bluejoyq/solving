import sys
input = sys.stdin.readline
N,M = map(int, input().split())
values = [list(map(int,input().split())) for i in range(N)]



def valid_val(r, c):
    if 0 > r or N - 1 < r:
        return 0
    return values[r][c]

result = 0
for r in range(N):
    for c in range(M-1):
        max_sum = 0
        max_sum = max(max_sum, values[r][c] * 2 + values[r][c+1] + valid_val(r - 1,c))
        max_sum = max(max_sum, values[r][c] * 2 + values[r][c+1] + valid_val(r + 1,c))
        max_sum = max(max_sum, values[r][c] + values[r][c+1] * 2 + valid_val(r - 1,c + 1))
        max_sum = max(max_sum, values[r][c] + values[r][c+1] * 2+ valid_val(r + 1,c + 1))
        result = max(result, max_sum)


print(result)