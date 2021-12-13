# 각 level의 수를 비교해야함.
import sys
from collections import deque
input =sys.stdin.readline
sys.setrecursionlimit(1000000)
N = int(input())

edges = [{} for i in range(N)]
for i in range(N-1):
	u,v = map(int, input().split())
	edges[u-1][v-1] = 1
	edges[v-1][u-1] = 1

visited = [0] * N
cache = [N] * N
def dfs(cur, is_essential):
	visited[cur] = 1
	selected_result = 1
	not_selected_result = 0

	for nxt in edges[cur].keys():
		if visited[nxt]:
			continue
		selected_result += dfs(nxt, 0)
	if is_essential:
		visited[cur] = 0
		return selected_result

	for nxt in edges[cur].keys():
		if visited[nxt]:
			continue
		not_selected_result += dfs(nxt, 1)
	visited[cur] = 0
	return min(selected_result,not_selected_result)
	

print(dfs(0, 0))