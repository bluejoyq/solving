import sys
sys.setrecursionlimit(1000000)
from collections import deque
input = sys.stdin.readline

N,R,Q = map(int,input().split())

edges = {i : {} for i in range(1,N+1)}

for i in range(N - 1):
	U,V = map(int, input().split())
	edges[U][V] = 1
	edges[V][U] = 1


nodes = [1] * (N + 1)
'''
def dfs(cur):
	for nxt in edges[cur].keys():
		del edges[nxt][cur]
		nodes[cur] += dfs(nxt)
	return nodes[cur]

dfs(R)
'''	




result = []
for i in range(Q):
	q_node = int(input())
	result.append(str(nodes[q_node]))

print('\n'.join(result))