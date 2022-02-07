import sys
input = sys.stdin.readline
from collections import deque
T = int(input())

def solve():
    N,K = map(int,input().split())
    taken_times = [0] +  list(map(int, input().split()))
    edges = [{} for i in range(N+1)]
    in_edge_count =[0] * (N + 1)
    for i in range(K):
        x,y = map(int,input().split())
        edges[x][y] = 1
        in_edge_count[y] += 1
        
    W = int(input())
    findings = deque([])

    cache = [0] * (N+1)
    for idx in range(1, N + 1):
        if in_edge_count[idx] > 0:
            continue
        findings.append((0, idx))
    
    while findings:
        cur_cost, cur = findings.popleft()
        if cur == W:
            return max(cache[cur], cur_cost + taken_times[cur])
        for nxt in edges[cur].keys():
            in_edge_count[nxt] -= 1
            cache[nxt] = max(cache[nxt], cur_cost + taken_times[cur])
            if in_edge_count[nxt] > 0:
                continue
            findings.append((cache[nxt] , nxt))
    
answer = []
for _ in range(T):
    answer.append(str(solve()))
print('\n'.join(answer))