N = int(input())

cache = [999] * (N + 1)
for i in range(1, N**0.5 +1):
    cache[i ** 2] = 1
    