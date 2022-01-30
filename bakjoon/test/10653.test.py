import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def solve_a(N,K,nodes):
    def get_dist(cur, nxt):
        return abs(nodes[cur][0] - nodes[nxt][0]) + abs(nodes[cur][1] - nodes[nxt][1])

    # dist, cur, jumped
    heap = [(0,0,0)]
    visited = [[0] * (K+ 1) for i in range(N)]
    while heap:
        cur_dist, cur, jumped = heappop(heap)
        if visited[cur][jumped]:
            continue
        visited[cur][jumped] = 1
        if cur == N - 1:
            break
        for jump in range(1, K - jumped + 2):
            nxt = cur + jump
            if nxt == N:
                break
            if visited[nxt][jumped + jump - 1]:
                continue
            heappush(heap, (cur_dist + get_dist(cur,nxt), nxt, jumped + jump - 1))
    return(cur_dist)


def solve_b(N,K,nodes):
    MAX = 9876543210
    cache = [[MAX] * (K + 1) for i in range(N)]

    def get_dist(cur, nxt):
        return abs(nodes[cur][0] - nodes[nxt][0]) + abs(nodes[cur][1] - nodes[nxt][1])
    cache[0][0]= 0
    for cur in range(N):
        for jump in range(min(K + 1, N - cur - 1)):
            nxt = cur + jump + 1
            dist = get_dist(cur,nxt)
            cache[nxt][jump] = min(cache[nxt][jump], cache[cur][0] + dist)
            for jumped in range(1,min(K-jump + 1,K + 1)):
                if cache[cur][jumped] == MAX:
                    break
                cache[nxt][jumped + jump] = min(cache[nxt][jumped + jump], cache[cur][jumped] + dist)
    return(min(cache[N-1]))


'''N, K = map(int, input().split())

nodes = [list(map(int,input().split())) for i in range(N)]
a= solve_a(N,K,nodes)
b = solve_b(N,K,nodes)
print(a,b)'''
import random

N = 10
K = 5
while True:
    nodes = [[random.randint(-10,10), random.randint(-10,10)] for i in range(N)]
    a= solve_a(N,K,nodes)
    b = solve_b(N,K,nodes)
    if a != b:
        for node in nodes:
            print(*node)
        print(a,b)
        break
