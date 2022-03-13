import sys
input = sys.stdin.readline

T = int(input())


def solve():
    N = int(input())

    root = {}
    values = []
    for i in range(N):
        values.append(list(input().rstrip()))
    for i in range(N):
        nums = values[i]
        cur = root
        for num in nums:
            try:
                cur = cur[num]
            except:
                cur[num] = {}
                cur = cur[num]
          
        cur[0] = 1
    for i in range(N):
        nums = values[i]
        cur = root
        for num in nums[:-1]:
            cur = cur[num] 
            try:
                cur[0]
                return 'NO'
            except:
                pass
    return 'YES'

for i in range(T):
    print(solve())