import sys
MAX = sys.maxsize
N = int(input())

cache = [MAX] * 100005
cache[1] = 1
cache[0] = 0
for i in range(N):
    for j in range(1,int((N-i) ** 0.5) + 1):
        cache[i + j ** 2] = min(cache[i+ j**2] , cache[i] + 1)

print(cache[N])