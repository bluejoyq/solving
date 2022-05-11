import random
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def solve1(N, K, values):
    cache = [0] * (K + 1)

    for cur_value in values:
        v = []
        for weight in range(K+1 - cur_value[0]):
            if cache[weight] == 0 or cache[
                    weight + cur_value[0]] > cache[weight] + cur_value[1]:
                continue
            v.append(weight)

        for weight in v:
            cache[weight + cur_value[0]
                  ] = max(cache[weight + cur_value[0]], cache[weight] + cur_value[1])
        if cur_value[0] > K:
            continue
        cache[cur_value[0]] = max(cache[cur_value[0]], cur_value[1])
    return(max(cache))


def solve2(N, K, values):
    cache = [0] * 100001
    for i in range(100001):
        cache[i] = [-1] * 101

    def select_best(weight, start):
        if start == N:
            return 0
        if cache[weight][start] != -1:
            return cache[weight][start]
        cache[weight][start] = select_best(weight, start + 1)
        if K >= (weight + values[start][0]):
            cache[weight][start] = max(cache[weight][start], select_best(
                weight + values[start][0], start + 1) + values[start][1])
        return cache[weight][start]

    return(select_best(0, 0))


while True:
    N = random.randint(1, 5)
    K = random.randint(1, 10)
    values = [[random.randint(1, 10), random.randint(1, 5)]
              for i in range(N)]
    answer1 = solve1(N, K, values)
    answer2 = solve2(N, K, values)
    if answer1 != answer2:
        break
print(N, K)
for val in values:
    print(*val)

print("=----")
print(answer1, answer2)
