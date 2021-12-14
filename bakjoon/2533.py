# 각 level의 수를 비교해야함.
import sys
input =sys.stdin.readline
N = int(input())

edges = [{} for i in range(N + 1)]
for i in range(N-1):
	u,v = map(int, input().split())
	edges[u][v] = 1
	edges[v][u] = 1

visited = [0] * (N + 1)
cache = [[0,1] for i in range(N + 1)] 
parents = [0] * (N+1)
result = 0
visited_nodes = []
findings = [1]

while findings:
	cur = findings.pop()
	visited[cur] = 1
	visited_nodes.append(cur)

	for nxt in edges[cur].keys():
		if visited[nxt]:
			parents[cur] = nxt
			continue
		
		findings.append(nxt)

while visited_nodes:
	child = visited_nodes.pop()
	parent = parents[child]

	cache[parent][1] += min(cache[child][0], cache[child][1])
	cache[parent][0] += cache[child][1]

print(min(cache[1]))