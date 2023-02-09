import sys
from collections import deque
input = sys.stdin.readline

def solve():
    result = 0
    N, M = map(int, input().split())
    goods = list(map(int, input().split()))
    costs = deque(sorted(map(int, input().split())))
    goods.sort()
    for i in range(min(M,N)):
        good = goods.pop()
        cost=  costs.popleft()
        if good - cost < 0:
            break
        result +=good - cost
    return result
print(solve())