import sys
input = sys.stdin.readline
MAX = sys.maxsize
N = int(input())
cache = [[MAX] * N for i in range(N)]
a,b = map(int,input().split())
while a != -1:
    cache[a - 1][b - 1] = 1
    cache[b - 1][a - 1] = 1
    a,b = map(int,input().split())




for i in range(N):
    cache[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            cache[i][j] = min(cache[i][j], cache[i][k] + cache[k][j])

# 최솟값 갱신
min_val = MAX
min_nodes = []
for i in range(N):
    val = max(cache[i])

    if val < min_val:
        min_nodes = []
        min_nodes.append(i + 1)
        min_val = val
    elif val == min_val:
        min_nodes.append(i + 1)
       
print(min_val, len(min_nodes))
print(*sorted(min_nodes))