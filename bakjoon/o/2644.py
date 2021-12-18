import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
target = list(map(int,input().split()))
M = int(input())

edges = [{} for i in range(N+1)]
for i in range(M):
	x,y = map(int,input().split())
	edges[x][y] = 1
	edges[y][x] = 1


# bfs
def bfs():
	findings = deque([(target[0], 0)])
	visited = [0] * (N+1)
	while findings:
		cur,val = findings.popleft()
		visited[cur] = 1

		for nxt in edges[cur].keys():
			if visited[nxt]:
				continue
			if nxt == target[1]:
				return(val + 1)
			findings.append((nxt, val + 1))
	return -1
print(bfs())