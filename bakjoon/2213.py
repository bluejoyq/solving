import sys
input = sys.stdin.readline

N = int(input())
nodes = list(map(int,input().split()))

edges = [{} for i in range(N)]

for i in range(N-1):
	a,b= map(int, input().split())
	edges[a - 1][b - 1] = 1
	edges[b - 1][a - 1] = 1

cache = [[0,0] for i in range(N)]
visited = [0] * N
findings = [0]
visited_nodes = []

while findings:
	cur = findings.pop()
	visited[cur] = 1
	visited_nodes.append(cur)
	cache[cur][1] += nodes[cur]
	for nxt in edges[cur].keys():
		if visited[nxt]:
			continue
		cache[nxt][0] = cache[cur][1]
		cache[nxt][1] = min(cache[cur][1], cache[cur][0])
		findings.append(nxt)


max_val = max(cache[N - 1])
max_idx = N-1
result = []


print(visited_nodes, cache)
for i in range(1, N):
	bef = visited_nodes[i-1]
	cur = visited_nodes[i]

	print(cache[cur])
result.sort()
print(result)