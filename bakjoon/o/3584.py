import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
T = int(input())

def solve():
    N = int(input())
    edges = [{} for i in range(N+1)]
    parents = [0] * (N + 1)
    for i in range(N - 1):
        a,b = map(int,input().split())
        edges[a][b] = 1
        parents[b] = a
    A,B = map(int,input().split())
    visited = [0] * (N + 1)

    def find_parent(cur):
        if cur == parents[cur] or visited[cur]:
            return cur
        else:
            visited[cur] = 1
            return find_parent(parents[cur])

    find_parent(A)
    return find_parent(B)

for i in range(T):
    print(solve())