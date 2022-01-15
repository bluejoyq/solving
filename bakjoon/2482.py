N = int(input())
K = int(input())


# 0번째 고르는 경우 
cache = [[0] * (K + 1) for i in range(N)]
cache[0][1] = 1
for i in range(1,N):
    for j in range(K + 1):
        cache[i][j] = cache[i - 1][j] + cache[i-2][j-1]
zero_pick = cache[N][K]
print(cache)
cache = [[0] * (K + 1) for i in range(N)]
cache[0][0] = 1
for i in range(1,N):
    for j in range(K + 1):
        cache[i][j] = cache[i - 1][j] + cache[i-2][j-1]
print(cache)
print(zero_pick + cache[N-1][K])