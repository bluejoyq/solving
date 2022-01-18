import sys
input = sys.stdin.readline
from collections import deque
N = int(input())


def solve():
    a,b,c = input().split()

    a_idx = 0
    b_idx = 0
    visited = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
    candidates = deque([(0, a_idx,b_idx)])
    
    while candidates:
        c_idx, a_idx, b_idx = candidates.pop()
        if a_idx < len(a) and a[a_idx] == c[c_idx]:
            if c_idx + 1 == len(c):
                return 1
            if visited[a_idx + 1][b_idx]:
                continue
            visited[a_idx + 1][b_idx]=1
            candidates.append((c_idx + 1,a_idx + 1, b_idx))
        if b_idx < len(b) and b[b_idx] == c[c_idx]:
            
            if c_idx + 1 == len(c):
                return 1
            if visited[a_idx][b_idx + 1]:
                continue
            visited[a_idx][b_idx + 1] = 1 
            candidates.append((c_idx + 1,a_idx, b_idx + 1))
    return 0

for i in range(N):
    result = solve()
    okay = 'no'
    if result:
        okay = 'yes'
    
    print(f'Data set {i+1}: {okay}')
