import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
def multiple_input():
    return map(int,input().split())
def solve():
    N = int(input())
    
    edges = [{} for i in range(N + 1)]
    inner_edge_count = [0] * (N+1)  

    values = list(multiple_input())
    for i in range(N-1):
        for j in range(i + 1, N):
            edges[values[i]][values[j]] = 1
            inner_edge_count[values[j]] += 1

    M = int(input())
    tmp = [list(multiple_input()) for i in range(M)]
    for i in range(M):
        a,b = tmp[i]
        try:
            del edges[a][b]
            inner_edge_count[b] -= 1
            edges[b][a] = 1
            inner_edge_count[a] += 1
            continue
        except:
            pass
        try:
            del edges[b][a]
            inner_edge_count[a] -= 1
            edges[a][b] = 1
            inner_edge_count[b] += 1
        except:
            pass
        
    
    # 어차피 1등부터 들어감
    findings = deque([])
    for i in range(1,N+1):
        if inner_edge_count[i] > 0:
            continue
        findings.append(i)

    visited_nodes = []
    while findings:
        cur = findings.popleft()
        visited_nodes.append(cur)
        for nxt in edges[cur].keys():
            inner_edge_count[nxt] -= 1
            if inner_edge_count[nxt] > 0:
                continue
            findings.append(nxt)
    if len(visited_nodes) == N:
        return ' '.join(map(str, visited_nodes))
    else:
        return 'IMPOSSIBLE'

answer = []
for _ in range(T):
    result = solve()
    answer.append(result)
print('\n'.join(answer))