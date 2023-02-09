import sys
MAX = sys.maxsize
N = int(input())

values = []
for i in range(N):
    row = list(map(int, input().split()))
    values.append(row)
max_result = -MAX



print(max_result)
