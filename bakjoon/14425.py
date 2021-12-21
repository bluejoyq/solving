import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = {}
for i in range(N):
    tmp = input().rstrip()
    S[tmp] = 1
result = 0
for i in range(M):
    tmp = input().rstrip()
    try:
        S[tmp]
        result += 1
    except:
        continue
print(result)