import sys 
input = sys.stdin.readline
from heapq import heappush, heappop

def input_edges(N,M):
    edges = [{} for i in range(N + 1)]
    input_edges_count = [0] * (N + 1)
    for i in range(M):
        a,b = map(int, input().split())
        edges[a][b] = 1
        input_edges_count[b] += 1
    return edges, input_edges_count



def solve():
    result = []
    N,M = map(int,input().split())
    edges, input_edges_count = input_edges(N,M)
    
    findings = []
    visited = [0] * (N+1)
    for i in range(1,N + 1):
        if input_edges_count[i]:
            continue
        heappush(findings, i)
        visited[i] = 1
    def find_nxt(cur):
        for nxt in edges[cur].keys():
            input_edges_count[nxt] -= 1
            if input_edges_count[nxt]:
                continue
            heappush(findings, nxt)
            visited[nxt] = 1
    while findings:
        cur = heappop(findings)
        find_nxt(cur)
        
        result.append(cur)
        
    print(*result)
solve()



 
    