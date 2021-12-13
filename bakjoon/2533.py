# 각 level의 수를 비교해야함.
import sys
input =sys.stdin.readline
N = int(input())

edges = [{} for i in range(N)]
for i in range(N-1):
	u,v = map(int, input().split())
	edges[u-1][v-1] = 1
	edges[u-1][v-1] = 1

# 각 레벨의 노드 수 구하기
visited = [0] * N
node_count_by_level = [0] * N
nxt_findings = [0]
cur_level = 0
while nxt_findings:
	findings = nxt_findings
	nxt_findings = []
	node_count_by_level[cur_level] = len(findings)
	cur_level += 1
	
	while findings:
		cur = findings.pop()
		visited[cur] = 1
		for nxt in edges[cur].keys():
			if visited[nxt]:
				continue
			nxt_findings.append(nxt)

# dp
cache= [[N,N] for i in range(N+2)]
cache[0][0] = 0
for i in range(N):
	if node_count_by_level[i] == 0:
		print(min(cache[i]), cache)
		print(node_count_by_level)
		break
	cache[i+1][1] = min(cache[i + 1][1],cache[i][0])
	cache[i+1][0] = min(cache[i + 1][0],cache[i][1] + node_count_by_level[i])


