import sys
from collections import deque
input = sys.stdin.readline

def multiple_input():
    return map(int,input().split())


N,M = multiple_input()

nodes = [[] for i in range(N + 1)]
nxt_count = [0] * (N + 1)
for i in range(M):
    a,b = multiple_input()
    nodes[a].append(b)
    nxt_count[b] += 1

que = deque([])
sort_node = []
for i in range(1,N + 1):
    if nxt_count[i] > 0:
        continue
    que.append(i)

while que:
    cur = que.popleft()
    sort_node.append(cur)
    for nxt in nodes[cur]:
        nxt_count[nxt] -= 1
        if nxt_count[nxt]> 0:
            continue
        que.append(nxt)
visited = [0] * (N+1)

for node in sort_node:
    visited[node] = 1
for i in range(1,N+1):
    if visited[i] == 0:
        sort_node.append(i)
print(*sort_node)