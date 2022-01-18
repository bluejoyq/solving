import sys
input = sys.stdin.readline
from bisect import bisect_left

def solve():
    N = int(input())
    points = [0]* N
    for i in range(N):
        points[i] = list(map(int, input().split()))
    result = 0
    for i in range(N - 2):
        for j in range(i+ 1,N - 1):
            line_ij = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2 
            for k in range(j+1, N):
                line_ik = (points[i][0] - points[k][0]) ** 2 + (points[i][1] - points[k][1]) ** 2 
                line_jk = (points[j][0] - points[k][0]) ** 2 + (points[j][1] - points[k][1]) ** 2 
                
                if line_ij + line_jk + line_ik - 2 * max(line_ij, line_jk, line_ik):
                    continue
                result += 1
    return result

print(solve())