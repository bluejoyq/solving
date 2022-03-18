import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def solve():
    N,M = map(int, input().split())
    edges = [{} for i in range(N+1)]

    for i in range(M):
        a,b,c = map(int, input().split())
        edges[a][b] = c
        edges[b][a] = c
    
    visited = [0] * (N+1)
    findings = [(0, 1)]
    selected_count = 0
    max_cur_cost = -1
    result = 0
    while selected_count < N:
        cur_cost, cur = heappop(findings)
        if visited[cur]:
            continue
        selected_count += 1
        visited[cur] = 1
        result += cur_cost
        max_cur_cost = max(cur_cost, max_cur_cost)
        for nxt in edges[cur].keys():
            if visited[nxt]:
                continue
            heappush(findings, (edges[cur][nxt], nxt))
    return result - max_cur_cost
print(solve())