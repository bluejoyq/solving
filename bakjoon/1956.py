# 유니온 파인드
# 

from heapq import heappush, heappop 
import sys
input= sys.stdin.readline
def solve():
    V,E = map(int, input().split())
    parents = [i for i in range(V + 1)]
    ranks = [0] * (V+1)

    def find(x):
        # 경로 압축 ㄴㄴ
        if x == parents[x]:
            return x
        return find(parents[x])

    def union(x,y):
        x = find(x)
        y = find(y)

        if x == y:
            return 0
        
        if ranks[x] > ranks[y]:
            parents[y] = x
            ranks[x] += 1
        else:
            parents[x] = y
            ranks[y] += 1
        return 1

    edges = []
    for i in range(E):
        a,b,c = map(int, input().split())
        heappush(edges,(c,a,b))

    edges_dict = [{} for i in range(V+1)]
    passed = 0
    # 일단 출발지와 도착지를 찾자.
    while edges:
        cost,a,b = heappop(edges)
        edges_dict[a][b] = cost
        if union(a,b):
            continue
        passed = 1
        break
    if not passed:
        return -1
    # 그리고 a에서 b로 가는 최단 루트 찾기
    visited = [0] *(V+1)
    print(a,b)
    findings = []
    for nxt in edges_dict[a].keys():
        if visited[nxt]:
            continue
        heappush(findings,(0 + edges_dict[a][nxt], nxt))
    while findings:
        cost,cur = heappop(findings)
        visited[cur] = 1
        if cur == a:
            return cost

        for nxt in edges_dict[cur].keys():
            if visited[nxt]:
                continue
            heappush(findings,(cost + edges_dict[cur][nxt], nxt))
print(solve())