import sys
from heapq import heappop,heappush


def find_possible_edges(cur,visited):
	edges = []
	for dim in range(3):
		cur_idx = original_idx[cur][dim]
		cur_val,_ = orderd_pos_by_dim[dim][cur_idx]
		if cur_idx > 0:
			nxt_val, nxt_idx = orderd_pos_by_dim[dim][cur_idx - 1]
			if visited[nxt_idx]:
				continue
			edges.append((nxt_idx,abs(cur_val - nxt_val)))
		if cur_idx <N-1:
			nxt_val, nxt_idx = orderd_pos_by_dim[dim][cur_idx + 1]
			if visited[nxt_idx]:
				continue
			edges.append((nxt_idx,abs(cur_val - nxt_val)))
	return edges

input = sys.stdin.readline
MAX = sys.maxsize
N = int(input())
# x,y,z순으로 정렬

original_idx = [[0]*3 for i in range(N)]
orderd_pos_by_dim = [[0] * N for i in range(3)]
for idx in range(N):
	tmp = list( map(int, input().split()))
	for dim in range(3):
		orderd_pos_by_dim[dim][idx] = (tmp[dim], idx)

for dim in range(3):
	orderd_pos_by_dim[dim].sort()

for j in range(N):
	for dim in range(3):
		_,idx = orderd_pos_by_dim[dim][j]
		original_idx[idx][dim] = idx

# 이제 prim으로 xyz 앞뒤만 보면됨!!!
result = 0
costs = [MAX] * N
visited = [0] * N
costs[0] = 0
findings = [(0,0)]
for i in range(N):
	cur, cur_cost = heappop(findings) 
	if visited[cur]:
		continue
	visited[cur] = 1
	for nxt,nxt_cost in find_possible_edges(cur,visited):
		if cur_cost + nxt_cost >= costs[nxt]:
			continue

		costs[nxt] = cur_cost + nxt_cost
		heappush(findings, (nxt, cur_cost + nxt_cost))

print(cur_cost)

