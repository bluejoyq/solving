import sys
input = sys.stdin.readline
from heapq import heappop, heappush
MAX = sys.maxsize
def solve():
    N,M = map(int, input().split())
    edges = [{} for i in range(N+1)]
    for i in range(M):
        A,B,C = map(int, input().split())
        try:
            edges[A][B] = max(C, edges[A][B])
        except:
            edges[A][B] = C
        try:
            edges[B][A] = max(C, edges[B][A])
        except:
            edges[B][A] = C
        
    
    visited = [0] * (N+1)
    S, E = map(int, input().split())
    findings = []
    heappush(findings, (-MAX, S))
    
    while findings:
        max_cost, cur = heappop(findings)
        
        if visited[cur]:
            continue
        visited[cur] = 1
        if cur == E:
            return max_cost
        for nxt in edges[cur].keys():
            if visited[nxt]:
                continue
            heappush(findings, (max(max_cost, -edges[cur][nxt]), nxt))
            

print(-solve())