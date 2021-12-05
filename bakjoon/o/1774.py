import sys
input = sys.stdin.readline

def find(x):
	if x == parents[x]:
		return x
	parents[x] = find(parents[x])
	return parents[x]

def union(x,y):
	x = find(x)
	y = find(y)
	if x == y:
		return True
	
	if ranks[x] > ranks[y]:
		ranks[x] += ranks[y]
		parents[y] = x
	else:
		ranks[y] += ranks[x]
		parents[x] = y 
	return False

def get_distance(a,b):
	return (abs(a[0] - b[0]) ** 2 + abs(a[1] - b[1]) ** 2)** 0.5

N,M= map(int, input().split())
nodes = [0] * N
edges = []
ranks = [1] * N
parents = [i for i in range(N)]
result = 0
for i in range(N):
	nodes[i] = list(map(int, input().split()))


for i in range(M):
	x,y = map(int, input().split())
	union(x- 1,y - 1)

for cur in range(N):
	for nxt in range(N):
		if cur == nxt:
			continue
		edges.append((get_distance(nodes[cur], nodes[nxt]), cur, nxt))

edges.sort()

for cost,cur,nxt in edges:
	if union(cur,nxt):
		continue
	result += cost

print(format(result,".2f"))