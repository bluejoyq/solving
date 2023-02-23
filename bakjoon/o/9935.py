values = input()
boom = input()

N = len(boom)
cache = []
for ch in values:
    cache.append(ch)
    while ''.join(cache[-N:]) == boom:
        for i in range(N):
            cache.pop()

if cache:
    print(''.join(cache))
else:
    print("FRULA")