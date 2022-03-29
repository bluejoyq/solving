NXTS = [[0,1], [0,-1], [1,0], [-1,0]]

def get_input():
    return [list(map(int, input().split())) for i in range(N)]

def is_valid_ice(values, visited,row,col):
    if (not values[row][col]) or visited[row][col]:
        return 0
    return 1
def is_valid_pos(row, col):
    if row < 0 or row > N -1 or col < 0 or col > M-1:
        return 0
    return 1

def melt(values,melt_ice):
    for r,c,melt_count in melt_ice:
        values[r][c]  = max(0, values[r][c] - melt_count)
def find_melt_ice(values,visited, row, col):
    ice = [(row,col)]
    melt_ice = []
    visited[row][col] = 1
    while ice:
        r,c = ice.pop()
        melt_count = 0
        for r_way, c_way in NXTS:
            nxt_r = r+r_way
            nxt_c = c+c_way
            if (not is_valid_pos(nxt_r, nxt_c)):
                continue
            if visited[nxt_r][nxt_c]:
                continue
            if values[nxt_r][nxt_c] == 0:
                melt_count += 1
                continue

            ice.append((nxt_r,nxt_c))
            
            visited[nxt_r][nxt_c] = 1
        melt_ice.append((r,c, melt_count))
    melt(values,melt_ice)

def melt_cycle(values):
    visited = [[0] * M for i in range(N)]
    fraction_flag = 0
    for row in range(N):
        for col in range(M):
            if not is_valid_ice(values, visited, row, col):
                continue
            if fraction_flag:
                return 0
            find_melt_ice(values,visited,row,col)
            fraction_flag = 1
    if fraction_flag == 0:
        return -1
    return 1
def main():
    values = get_input()
    for year in range(1, 102000):
        melt_info = melt_cycle(values)
        if melt_info == -1:
            return 0
        elif melt_info == 0:
            return year - 1

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
print(main())