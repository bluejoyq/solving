import sys
input = sys.stdin.readline

M = int(input())
edges = [{} for i in range(M+1)]
for i in range(1, M + 1):
    edges[i][int(input())] = 1

Q = int(input())
for i in range(Q):
    n,x = map(int, input().split())
    