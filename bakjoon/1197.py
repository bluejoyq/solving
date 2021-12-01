import sys
input = sys.stdin.readline

V,E = map(int, input().split())
edges = []
parents = [i for i in range(V+1)]
ranks = [1] * (V+ 1)
result = 0
def find(x):
	if x == parents[x]:
		return x
	return find(parents[x])

def union(x,y):
	x = find(x)
	y = find(y)

	if x == y:
		return False
	
	if ranks[x] > ranks[y]:
		parents[y] = x
		ranks[x] += ranks[y]
	else:
		parents[x] = y
		ranks[y] += ranks[x]
	return True

for i in range(E):
	a,b,c = map(int, input().split())
	edges.append((c,a,b))

edges.sort()
for c,a,b in edges:
	if union(a,b):
		result += c
	
print(result)