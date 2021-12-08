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

cache[0][1] += nodes[0]
while findings:
	cur = findings.pop()
	visited[cur] = 1
	cache[cur][1] += nodes[cur]
	for nxt in edges[cur].keys():
		if visited[nxt]:
			continue
		cache[nxt][0] = cache[cur][1] + nodes[nxt]
		cache[nxt][1] = cache[cur][0]
		findings.append(nxt)

max_val = -1
max_idx = [-1,-1]
for i in range(N):
	if max_val < cache[i][0]:
		max_val = cache[i][0]
		max_idx = [i,0]
	if max_val < cache[i][1]:
		max_val = cache[i][1]
		max_idx = [i,1]
print(max_val)
print(*max_idx)
result = []
cur = max_idx[0]
cur_sub = max_idx[1]
while max_val > 0:
	max_val -= nodes[cur]
	result.append(cur + 1)
	visited[cur] = 2

	for nxt in edges[cur].keys():
		if visited[nxt] == 2:
			continue
		if max_val == cache[nxt][1- cur_sub]:
			cur = nxt
			cur_sub = 1-cur_sub
			break
result.sort()
print(result)