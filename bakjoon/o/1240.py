import sys
input = sys.stdin.readline
N, M = map(int, input().split())

edges = [{} for i in range(N + 1)]

for i in range(N - 1):
    a, b, c = map(int, input().split())
    edges[a][b] = c
    edges[b][a] = c

for i in range(M):
    a, b = map(int, input().split())
    visited = [0] * (N + 1)

    findings = [(0, a)]
    visited[a] = 1
    while findings:
        cur_cost, cur = findings.pop()

        if cur == b:
            print(cur_cost)
            break
        for nxt in edges[cur].keys():
            if visited[nxt]:
                continue
            visited[nxt] = 1
            findings.append((cur_cost + edges[cur][nxt], nxt))
