# 각 level의 수를 비교해야함.
import sys
from collections import deque
input =sys.stdin.readline
sys.setrecursionlimit(1000000)
N = int(input())

edges = [{} for i in range(N + 1)]
for i in range(N-1):
	u,v = map(int, input().split())
	edges[u][v] = 1
	edges[v][u] = 1

visited = [0] * (N + 1)
cache = [[0,0] for i in range(N + 1)] 
result = 0

findings = [1]

def dfs(cur):
	visited[cur] = 1
	cache[cur][1] =  1
	for nxt in edges[cur].keys():
		if visited[nxt]:
			continue
		dfs(nxt)
		cache[cur][1] += min(cache[nxt][1],cache[nxt][0])
		cache[cur][0] += cache[nxt][1]
dfs(1)
print(min(cache[1]))