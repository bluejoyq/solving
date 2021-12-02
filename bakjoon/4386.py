import sys
from collections import deque
input = sys.stdin.readline

def get_distance(a,b):
	return (abs(a[0] - b[0]) ** 2 + abs(a[1] - b[1]) ** 2)** 0.5

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
		parents[y] = x
		ranks[x] += ranks[y]
	else:
		parents[x] = y
		ranks[y] += ranks[x]
	return False

N = int(input())

nodes = [0]*N
edges = []
parents = [i for i in range(N)]
ranks = [1] * N

for i in range(N):
	nodes[i] = list(map(float, input().split()))


for i in range(N):
	for j in range(N):
		if i == j:
			continue
		edges.append((get_distance(nodes[i], nodes[j]), i, j))
edges.sort()
result = 0
edges_count = 0

for c,a,b in edges:
	if edges_count > N - 1:
		break
	if union(a,b):
		continue
	edges_count += 1
	result += c
print(round(result,2))