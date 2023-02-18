N,K = map(int,input().split())

values = list(map(int,input().split()))

cur = sum(values[:K])
result = cur
for i in range(K, N):
    cur += values[i]
    cur -= values[i - K]
    result = max(result, cur)

print(result)