import sys
input = sys.stdin.readline
T = int(input())

def solve():
    targets = input().rstrip()
    left_count = 0
    for ch in targets:
        if ch == '(':
            left_count += 1
        elif left_count > 0:
            left_count -= 1
        else:
            return "NO"
    if left_count == 0:
        return "YES"
    return "NO"
result =[]
for i in range(T):
    result.append(solve())
print('\n'.join(result))