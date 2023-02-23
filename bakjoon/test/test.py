from itertools import permutations
a = [i for i in range(10)]


result = []

for i in range(1, 6):
    for val in permutations(a, i):
        result.append(val)


print(len(result))