import sys
input = sys.stdin.readline

N, K = map(int, input().split())

values = [list(map(int, input().split())) for i in range(N)]
cache = [0] * (K + 1)

for cur_value in values:
    v = []
    for weight in range(K+1 - cur_value[0]):
        if cache[weight] == 0 or cache[
                weight + cur_value[0]] > cache[weight] + cur_value[1]:
            continue
        v.append(weight)
    if cur_value[0] > K:
        continue
    cache[cur_value[0]] = max(cache[cur_value[0]], cur_value[1])
    for weight in reversed(v):
        cache[weight + cur_value[0]
              ] = max(cache[weight + cur_value[0]], cache[weight] + cur_value[1])
print(max(cache))
