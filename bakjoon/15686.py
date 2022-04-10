import sys
input = sys.stdin.readline
MAX = sys.maxsize
N,M = map(int, input().split())
board = [list(map(int,input().split())) for i in range(N)]


chickens = []
homes = []
for r in range(N):
    for c in range(N):
        if board[r][c] == 2:
            chickens.append((r,c))
        elif board[r][c] == 1:
            homes.append((r,c))


visited = [[MAX] * M for i in range(N)]
searchs = [[0,1], [1,0], [-1,0], [0,-1]]

while chickens:
    start_r, start_c = chickens.pop()
    findings = [(start_r,start_c, 1)]
    visited[start_r][start_c] = 0
    while findings:
        r,c,distance = findings.pop()

        for r_plus, c_plus in searchs:
            nxt_r = r + r_plus
            nxt_c = c + c_plus

            if nxt_r > N - 1 or nxt_r < 0 or nxt_c > M-1 or nxt_c < 0:
                continue

            if visited[nxt_r][nxt_c] < distance:
                continue
            visited[nxt_r][nxt_c] = distance
            
            findings.append((nxt_r,nxt_c, distance + 1))
result = 0
for r,c in homes:
    result += visited[r][c]
print(result)