import sys
input = sys.stdin.readline
from heapq import heappush, heappop
MAX = 9876543210
def solve():
    R,C = map(int,input().split())
    
    board = [0] * R
    for i in range(R):
        board[i] = list(input().rstrip())
    
    cache = [[0] * C for i in range(R)]
    SEARCH_RANGES = [[1,0], [0,1], [-1,0], [0,-1]]
    start = []


    def wrong_range(new_r,new_c):
        if new_r < 0 or new_r > R-1 or new_c < 0 or new_c > C-1:
            return 1
        return 0
    def find_ice():
        melt_list = []
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'X':
                    cache[r][c] = MAX
                    continue
                if board[r][c] == 'L':
                    cache[r][c] = -1
                    start.append([r,c])
                    continue
                melt_list.append((r,c))
        return melt_list

    def melt_ice(counting, melt_list):
        new_melt_list = []
        for r,c in melt_list:
            for r_p, c_p in SEARCH_RANGES:
                new_r = r+r_p
                new_c = c+c_p
                if wrong_range(new_r,new_c):
                    continue
                if board[new_r][new_c] != 'X' or cache[new_r][new_c] <= counting:
                    continue
                cache[new_r][new_c] = counting
                new_melt_list.append((new_r,new_c))
        return new_melt_list

    melt_list = find_ice()
    for counting in range(1,MAX):
        melt_list = melt_ice(counting, melt_list)
        if not melt_list:
            break
    
    visited = [[-1] * C for i in range(R)]
    findings = []
    start_r, start_c = start[0]
    heappush(findings, (0, start_r, start_c))
    cache[start_r][start_c] = 0

    while findings:
        cur_cost, r,c = heappop(findings)
        visited[r][c] = cur_cost
        if cache[r][c] == -1:
            break
        for r_p, c_p in SEARCH_RANGES:
            new_r = r+r_p
            new_c = c+c_p
            if wrong_range(new_r,new_c)or visited[new_r][new_c] != -1:
                continue
            heappush(findings, (max(cur_cost, cache[new_r][new_c]), new_r, new_c))
    print(cur_cost)
solve()