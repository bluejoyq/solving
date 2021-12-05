import sys

def find_possible_edges():
	edges = []
	for cur in range(N):
		for dim in range(3):
			cur_idx = original_idx[cur][dim]
			cur_val,_ = orderd_pos_by_dim[dim][cur_idx]
			if cur_idx > 0:
				nxt_val, nxt_idx = orderd_pos_by_dim[dim][cur_idx - 1]
				edges.append((abs(cur_val - nxt_val),cur,nxt_idx))
			if cur_idx <N-1:
				nxt_val, nxt_idx = orderd_pos_by_dim[dim][cur_idx + 1]
				edges.append((abs(cur_val - nxt_val),cur,nxt_idx))
	return edges

def find(x):
	if x == parents[x]:
		return x
	parents[x] = find(parents[x])
	return parents[x]

def union(x,y):
	x = find(x)
	y = find(y)
	if x == y:
		return None
	if ranks[x] > ranks[y]:
		ranks[x] += ranks[y]
		parents[y] = x
	else:
		ranks[y] += ranks[x]
		parents[x] = y
	return True

input = sys.stdin.readline
MAX = sys.maxsize
N = int(input())
parents = [i for i in range(N)]
ranks = [1] * N
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
		original_idx[idx][dim] = j

# 이제 prim으로 xyz 앞뒤만 보면됨!!!
result = 0
costs = [MAX] * N
visited = [0] * N
edges = find_possible_edges()
edges.sort()

for cost,cur,nxt in edges:
	if union(cur,nxt) == None:
		continue
	
	result += cost

print(result)