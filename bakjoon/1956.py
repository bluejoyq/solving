# 유니온 파인드
# 

from heapq import heappush, heappop 
import sys
input= sys.stdin.readline



def solve():
    V,E = map(int, input().split())
    edges = [{} for i in range(V+1)]
    for i in range(E):
        a,b,c = map(int, input().split())
        edges[a][b] = c
    def find_fastest_cycle(start):
        visited = [0] *(V+1)
        findings = []
        for nxt in edges[start].keys():
            if visited[nxt]:
                continue
            heappush(findings,(0 + edges[start][nxt], nxt))
        while findings:
            cost,cur = heappop(findings)
            visited[cur] = 1
            if cur == start:
                return cost

            for nxt in edges[cur].keys():
                if visited[nxt]:
                    continue
                heappush(findings,(cost + edges[cur][nxt], nxt))
        return -1
    result = 9876543210
    for i in range(1, V+1):
        cost = find_fastest_cycle(i)
        if cost == -1:
            continue
        result = min(cost,result)
    if result == 9876543210:
        result = -1
    return result
    
print(solve())