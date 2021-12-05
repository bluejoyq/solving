import sys

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
edges = []
pos_by_dim = [[0] * N for i in range(3)]

for idx in range(N):
	vals = list(map(int, input().split()))
	for dim in range(3):
		pos_by_dim[dim][idx] = (vals[dim], idx)
# x,y,z순으로 정렬
for dim in range(3):
	pos_by_dim[dim].sort() 	

for dim in range(3):
	cur_val, cur = pos_by_dim[dim][0]
	nxt_val, nxt = pos_by_dim[dim][1]
	edges.append((abs(cur_val - nxt_val), cur, nxt))


	for idx in range(1,N):
		cur_val, cur = pos_by_dim[dim][idx]
		nxt_val, nxt = pos_by_dim[dim][idx- 1]
		edges.append((abs(cur_val - nxt_val), cur, nxt))
result = 0
costs = [MAX] * N
visited = [0] * N
edges.sort()

for cost,cur,nxt in edges:
	if union(cur,nxt) == None:
		continue
	
	result += cost

print(result)