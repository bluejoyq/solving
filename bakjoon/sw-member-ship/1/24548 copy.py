import sys
input = sys.stdin.readline

mapping = {"T": 0, "G" : 1, "F":2,"P":3}
def check(info):
    for i in info:
        if i % 3 != 0:
            return 0
    return 1
def solve():
    result = 0
    N = int(input())
    data = input().rstrip()
    for i in range(3, N + 1, 3):
        cache = [0] * N
        info = [0,0,0,0]
        for ch in data[:i]:
            info[mapping[ch]] += 1
        
        cache[i - 1] = check(info)
        result += cache[i-1]
        for j in range(i, N):
            info[mapping[data[j]]] += 1
            info[mapping[data[j - i]]] -= 1
            if check(info):
                cache[j] += 1
                result += cache[j]

    return result
print(solve())