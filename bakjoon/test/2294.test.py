import random


def solve(n,k,values):
    MAX = 10001

    cache = [MAX] * (200001)

    values.sort(reverse=True)
    cache[0] = 0
    for val in values:

        for i in range(k + 1):
            cur = cache[i]

            if cur == MAX:
                continue
            if i + val == k:
                return min(cur + 1, cache[i + val])
                
            cache[i+val] = min(cur + 1, cache[i + val])

                
    return -1

def solve2(n,k,values):
    MAX = 10001

    cache = [MAX] * (200001)
    for val in values:
        cache[val] = 1


    for i in range(k + 1):
        if cache[i] == MAX:
            continue
        for val in values:
            if cache[i + val] <= cache[i] + 1:
                continue
            cache[i+val] = cache[i] + 1

    if cache[k] == MAX:
        return(-1)
    else:
        return(cache[k])


ans1 = 0
ans2 = 0
while ans1 == ans2:
    n = random.randint(1, 5)
    k = random.randint(1, 100)
    values = [random.randint(1,10) for i in range(n)]
    ans1 = solve(n,k,values)
    ans2 = solve2(n,k,values)

print(n, k)
print(*values)

print(ans1)
print(ans2)