from itertools import combinations
def solution(arr, m):
    N = len(arr)
    val = [0] * (N*N)
    
    for x in range(N):
        for y in range(N):
            val[x * N + y] = abs(arr[x] - arr[y])
    val.sort()
    return val[N*N - m - 1]