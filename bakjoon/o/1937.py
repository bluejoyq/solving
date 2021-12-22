import sys
from heapq import heappop, heappush
input = sys.stdin.readline
N = int(input())
values = [0] * N

for i in range(N):
    values[i] = list(map(int,input().split()))

min_values = []
for r in range(N):
    for c in range(N):
        heappush(min_values, (values[r][c],r,c))

cache = [[1] * N for i in range(N)]
search_ranges = [[0,1], [0,-1], [-1,0], [1,0]]
while min_values:
    cur_val, r,c = heappop(min_values)

    for r_plus, c_plus in search_ranges:
        new_r = r + r_plus
        new_c = c + c_plus
        if not (-1 < new_r < N and -1 < new_c < N):
            continue
        nxt_val = values[new_r][new_c]
        if cur_val >= nxt_val:
            continue

        cache[new_r][new_c] = max(cache[new_r][new_c], cache[r][c] + 1)

max_val = 1
for r in range(N):
    max_val = max(max_val,max(cache[r]))
print(max_val)