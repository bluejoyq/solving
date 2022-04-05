
import sys
from math import ceil
from bisect import bisect_right
input = sys.stdin.readline

def solve():
    N,H = map(int, input().split())
    upper_blocks = [0] * (N//2)
    under_blocks = [0] * ceil(N/2 - 0.1)
    for i in range(N):
        if i % 2 == 0:
            under_blocks[i // 2] = int(input())
        else:
            upper_blocks[i // 2] = H - int(input())
            
    upper_blocks.sort()
    under_blocks.sort()

    min_val = sys.maxsize
    min_count = 0
    for i in range(H):
        val = bisect_right(upper_blocks, i) + len(upper_blocks) - bisect_right(under_blocks,i)
        if min_val > val:
            min_count = 1
            min_val = val
        elif min_val ==val:
            min_count += 1  
    return min_val, min_count
print(*solve())