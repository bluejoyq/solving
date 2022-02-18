import sys
from collections import defaultdict
input = sys.stdin.readline

N,M,K = map(int, input().split())
edges = [defaultdict(int) for i in range(N + 1)]
for i in range(K):
    a,b,c = map(int, input().split())
    edges[a][b] = max(edges[a][b], c)

cache = [[-1] * M for i in range(N + 1)] 

cache[1][0] = 0
for cur in range(1, N+ 1):
    for selected in range(M - 1):
        if cache[cur][selected] == -1:
            continue
        for nxt in edges[cur].keys():
            if cache[nxt][selected + 1] == -1:
                cache[nxt][selected + 1] = 0
            cache[nxt][selected + 1] = max(cache[nxt][selected + 1] , cache[cur][selected] + edges[cur][nxt])
print(max(cache[N]))