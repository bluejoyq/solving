import sys
input = sys.stdin.readline
T = int(input())


for _ in range(T):
	N, M = map(int, input().split())
	edges = {i : {} for i in range(1,N + 1)}
	for i in range(M):
		a,b = map(int, input().split())
		edges[a][b] = 1
		edges[b][a] = 1
	
	# 가중치를 1로 두고 
	# 막다른 곳에서만 2로 해주면 된다.

	result = 0
	visited = [0] * (N + 1)
	findings = [1]
	while findings:
		cur = findings.pop()
		if visited[cur]:
			continue
		visited[cur] = 1
		is_dead_end = 1
		for nxt in edges[cur].keys():
			if visited[nxt]:
				continue
			findings.append(nxt)
			is_dead_end = 0
		result += 1

	
	print(result - 1)

'''
1
5 4
1 2
1 3
1 4
4 5

1
2 1
1 2
'''