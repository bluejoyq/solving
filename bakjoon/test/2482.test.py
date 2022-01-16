import unittest

def better_solution(N,K):

    LARGE_NUM = 1000000003
    # 0번째 고르는 경우 
    cache = [[0] * (K + 1) for i in range(N + 2)]
    cache[0][1] = 1
    cache[1][0] = 1
    result = 0
    for i in range(N - 1):
        for j in range(K):
            cache[i + 1][j] += cache[i][j]
            cache[i + 2][j+1] += cache[i][j]
        result += cache[i][K]

    return(result % LARGE_NUM)
def solution(N,K):

    LARGE_NUM = 1000000003
    # 0번째 고르는 경우 
    cache = [[0] * (K + 1) for i in range(N + 2)]
    cache[0][1] = 1
    result = 0
    for i in range(N - 1):
        for j in range(K):
            cache[i + 1][j] = (cache[i+1][j] + cache[i][j]) % LARGE_NUM
            cache[i + 2][j+1] = (cache[i + 2][j+1] + cache[i][j]) % LARGE_NUM
        result += cache[i][K]
    tmp = result

    # 0번째를 고르지 않는 경우
    cache = [[0] * (K + 1) for i in range(N + 2)]
    cache[1][0] = 1
    result = 0
    for i in range(1,N):
        for j in range(K):
            cache[i + 1][j] = (cache[i+1][j] + cache[i][j]) % LARGE_NUM
            cache[i + 2][j+1] = (cache[i + 2][j+1] + cache[i][j]) % LARGE_NUM
        result += cache[i][K]
    for i in range(N, N+2):
        result += cache[i][K]
    return((tmp + result) % LARGE_NUM)

import random

while True:
    N = random.randint(4,100)
    K = random.randint(4, N)
    assert(better_solution(N,K) == solution(N,K))
    print(N,K)