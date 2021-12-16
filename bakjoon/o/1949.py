import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N = int(input())
nodes = list(map(int,input().split()))
edges = [{} for i in range(N)]
for i in range(N-1):
	a,b = map(int,input().split())
	edges[a - 1][b - 1] = 1
	edges[b - 1][a - 1] = 1


cache = [[0,0] for i in range(N)]
visited = [0] * N

def dfs(cur):
	visited[cur] = 1
	cache[cur][1] = nodes[cur]
	for nxt in edges[cur].keys():
		if visited[nxt]:
			continue
		dfs(nxt)
		cache[cur][1] += cache[nxt][0]
		cache[cur][0] += max(cache[nxt][0], cache[nxt][1])

dfs(0)
print(max(cache[0]))