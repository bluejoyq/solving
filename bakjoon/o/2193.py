N = int(input())

cache = [[0,0] for i in range(N)]

cache[0][1] = 1
for i in range(N - 1):
    cache[i+1][1] = cache[i][0]
    cache[i+1][0] = sum(cache[i])
print(sum(cache[N-1]))