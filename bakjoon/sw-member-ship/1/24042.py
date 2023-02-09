import sys
from heapq import heappush, heappop
from bisect import bisect_left
input = sys.stdin.readline
N,M = map(int,input().split())
edges = [{} for i in range(N + 1)]
for i in range(M):
    A,B = map(int,input().split())
    try:
        edges[A][B].append(i)
    except:
        edges[A][B] = [i]
    try:
        edges[B][A].append(i)
    except:
        edges[B][A] = [i]
for edge in edges:
    for e in edges:
        e.sort()
findings = []
visited = [0] * (N + 1)
heappush(findings, (0, 1))
while findings:
    cur_time, cur_pos = heappop(findings)
    if visited[cur_pos]:
        continue
    if cur_pos == N:
        print(cur_time + 1)
    visited[cur_pos] = 1
    for nxt in edges[cur_pos]:
        if visited[nxt]:
            continue
        idx = bisect_left(nxt, cur_time % M)
        if idx > len(nxt):
            heappush(findings, (min_time,nxt))
        else:
            heappush(findings, (cur_time - (cur_time % M) ,nxt))