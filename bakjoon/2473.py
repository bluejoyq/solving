from itertools import combinations
N = int(input())
values = list(map(int,input().split()))

twin_values_idxs = list(combinations([i for i in range(N)], 2))
M = len(twin_values_idxs)
twin_values = [0] * M
for i in range(M):
    a,b = twin_values_idxs[i]
    twin_values[i] = (values[a] + values[b],a,b)

twin_values.sort()
values.sort()



twin_left = 0
right = N- 1

while True:
    val, a,b = twin_values[twin_left]
    if a == right or 
    std = val + values[right]