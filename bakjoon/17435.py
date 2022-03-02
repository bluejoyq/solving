import sys
sys.setrecursionlimit(5000001)
input = sys.stdin.readline

M = int(input())

values = [0] + list(map(int, input().split()))
cache = [{} for i in range(M+1)]
result = []
Q = int(input())

def find_nested_result(n,x):
    if n == 0:
        return x
    try:
        return cache[x][n]
    except:
        pass
    cache[x][n] = find_nested_result(n - 1, values[x])
    return cache[x][n]
for i in range(Q):
    n,x = map(int, input().split())
    result.append(str(find_nested_result(n,x)))
print('\n'.join(result))