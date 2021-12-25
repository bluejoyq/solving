N,S = map(int, input().split())
values = list(map(int,input().split()))

candidates = []
for value in values:
    c = len(candidates)
    for i in range(c):
        cadidate = candidates[i]
        candidates.append(cadidate + value)
    candidates.append(value)

result = 0
for cadidate in candidates:
    if cadidate == S:
        result += 1
print(result)