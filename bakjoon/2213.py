import sys
input = sys.stdin.readline

N = int(input())
nodes = [0] + list(map(int,input().split()))

edges = [{} for i in range(N + 1)]

for i in range(N-1):
	a,b= map(int, input().split())
	edges[a][b] = 1
	edges[b][a] = 1

cache = [[0,0] for i in range(N + 1)]
visited = [0] * (N+1)
findings = [1]
visited_nodes = []

def dfs(cur):
	visited[cur] = 1
	cache[cur][1] += nodes[cur]
	

	for nxt in edges[cur].keys():
		if visited[nxt]:
			continue
		findings.append(nxt)
		visited_nodes.append((cur, nxt))
		dfs(nxt)
		cache[cur][1] += cache[nxt][0]
		cache[cur][0] += max(cache[nxt][0] , cache[nxt][1])

dfs(1)
cur_val = max(cache[1])
print(cur_val)
result = {}

for parent, child in visited_nodes:
	print(parent,cache[parent], child, cache[child], cur_val)
	if max(cache[parent]) == max(cache[child]) + nodes[parent]:
		result[parent] = 1
print(*sorted(result.keys()))