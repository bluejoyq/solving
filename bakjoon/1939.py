import sys
input = sys.stdin.readline
from collections import deque
MAX = sys.maxsize
def solve():
    N,M = map(int, input().split())
    edges = [{} for i in range(N+1)]
    for i in range(M):
        A,B,C = map(int, input().split())
        edges[A][B] = C
        edges[B][A] = C
    
    
    S, E = map(int, input().split())
    findings = deque([])
    findings.append(S)
    visited = [0] * (N+1)
    cache = [MAX] * (N+1)
    while findings:
        cur = findings.popleft()
        if visited[cur] == 1:
            continue
        visited[cur] = 1
        for nxt in edges[cur].keys():
            nxt_max_cost = min(cache[cur], edges[cur][nxt])
            if cache[nxt] < nxt_max_cost:
                continue

            if cache[nxt] == MAX:
                cache[nxt] = nxt_max_cost
            else:
                cache[nxt] = max(nxt_max_cost, cache[nxt])
            findings.append(nxt)
    return cache[E]
print(solve())