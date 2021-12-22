N = int(input())

cache = [[0] * 10 for i in range(N)]
cache[0] = [1] * 10

for i in range(N-1):
    square_sum = 0
    for j in range(10):
        square_sum+= cache[i][j] % 10007
        cache[i+1][j] = square_sum
print(sum(cache[N-1]) % 10007)