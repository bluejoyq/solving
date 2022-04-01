import sys
input = sys.stdin.readline
MAX = sys.maxsize

N, M = map(int,input().split())
def input_values():
    return [list(map(int,input().split())) for i in range(N)]

def is_valid(r,c):
    if r > N - 1 or c > M - 1 or c < 0: 
        return 0
    return 1

def main():
    values = input_values()
    cache = [[[-MAX,-MAX]for i in range(M)] for j in range(N)]
    cache[0][0][1] = values[0][0]
    for r in range(N):
        for c in range(M):
            
            
            if is_valid(r, c+1):
                cache[r][c + 1][0] = max(cache[r][c + 1][0],max(cache[r][c]) + values[r][c+1])
        for c in range(M-1,-1,-1):
            if is_valid(r, c-1):
                cache[r][c - 1][1] = max(cache[r][c - 1][1],cache[r][c][1] + values[r][c-1])
            if is_valid(r + 1,c):
                cache[r + 1][c][1] = max(cache[r + 1][c][1],max(cache[r][c]) + values[r+1][c])
    return max(cache[N-1][M-1])
print(main())