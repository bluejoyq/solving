N = int(input())
cache = [0 for i in range(N+4)]

for i in range(N):
    turn = i % 2
    cache[i + 1] = turn
    cache[i + 3] = turn

if cache[N] == 0:
    print("SK")
else:
    print("CY")      