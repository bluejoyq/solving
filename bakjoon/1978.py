N = int(input())

# 소수면 1
cache = [i % 2 for i in range(1001)]
cache[1] = 0
cache[2]= 1
for i in range(3, 33):
    num = i * 2
    while num <= 1000:
        cache[num] = 0
        num += i

values = list(map(int, input().split()))
result = 0

for value in values:
    if cache[value] == 0:
        continue
    result += 1
print(result)
