import sys 
from heapq import heappush, heappop
input= sys.stdin.readline
MAX = 1000000
def solve():
    N = int(input())
    values = [0] * (MAX)
    for i in range(N):
        a,b = map(int, input().split())
        values[a]= max(values[a], b)

    L,P = map(int,input().split())

    can_move = P
    cur_pos = 0
    used_fuels = 0
    fuels = []
    
    while cur_pos < L:
        
        if values[cur_pos] > 0:
            heappush(fuels, -values[cur_pos])

        
        if can_move == 0:
            if not fuels:
                break
            used_fuels += 1
            can_move += -heappop(fuels)

        can_move -= 1
        cur_pos += 1
        
    
    if cur_pos == L:
        return used_fuels
    return -1

print(solve())