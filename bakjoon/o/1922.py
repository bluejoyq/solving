import sys
from heapq import heappop, heappush
input = sys.stdin.readline


N = int(input())
M = int(input())

edges = {i : {} for i in range(1, N+1)}
for i in range(M):
	a,b,c = map(int, input().split())
	edges[a][b] = c
	edges[b][a] = c

visited = [0] * (N + 1)
result = 0
possible_edges = []
heappush(possible_edges, (0,1))

while possible_edges:
	cost,cur = heappop(possible_edges)
	if visited[cur]:
		continue
	result += cost
	visited[cur] = 1
	
	for nxt in edges[cur].keys():
		if visited[nxt]:
			continue
		heappush(possible_edges,(edges[cur][nxt],nxt))
	

print(result)