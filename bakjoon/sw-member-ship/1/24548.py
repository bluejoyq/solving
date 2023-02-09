import sys
input = sys.stdin.readline

mapping = {"T": 0, "G" : 1, "F":2,"P":3}
def check(old, new):
    for i in range(4):
        if (new[i] - old[i]) % 3 != 0:
            return 0
    return 1
def solve():
    result = 0
    N = int(input())
    data = input().rstrip()
    cache = [[0,0,0,0] for i in range(N + 1)]
    for i in range(N):
        cache[i+1] = cache[i][:]
        cache[i + 1][mapping[data[i]]] += 1
    for i in range(3, N + 1, 3):
        for j in range(i, N+ 1):
            result += check(cache[j-i], cache[j])

    return result
print(solve())