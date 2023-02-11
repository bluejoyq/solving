MAX = 10001
n,k = map(int, input().split())

values = set([])
cache = [MAX] * (200001)
for i in range(n):
    val = int(input())
    cache[val] = 1
    values.add(val)


for i in range(k + 1):
    if cache[i] == MAX:
        continue
    for val in values:
        if cache[i + val] <= cache[i] + 1:
            continue
        cache[i+val] = cache[i] + 1

if cache[k] == MAX:
    print(-1)
else:
    print(cache[k])
