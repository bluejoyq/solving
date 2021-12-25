import sys
input = sys.stdin.readline
from heapq import heappush, heappop
from collections import deque
T = int(input())
# 거꾸로 생각하자.
# 시작 지점을 찾기 힘드니
# 끝지점에서 출발 ㅇㅇ
# 위상정렬 문제네 ㅋㅋㅋ;
def solve():
    N,K = map(int,input().split())
    taken_times = [0] +  list(map(int, input().split()))
    edges = [{} for i in range(N+1)]
    for i in range(K):
        x,y = map(int,input().split())
        edges[y][x] = 1 # 거꾸로
    W = int(input())
    
    visited = [0] * (N+1)
    possibles = deque([W])
    while possibles:      
        cur_node = possibles.popleft()
        print(visited[cur_node], cur_node)
        for nxt in edges[cur_node].keys():
            if visited[nxt]:
                visited[nxt] = max(visited[nxt] , taken_times[cur_node])
                continue
            possibles.append(nxt)
            visited[nxt] = taken_times[cur_node]
    print(sum(visited) + taken_times[cur_node])
for _ in range(T):
    solve()