import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
goal = deque([0] * n)
for i in range(n):
    goal[i] = int(input())

waiting_values = [i for i in range(1,n+1)]
stk =[0]
cur_num = 1
cur_match = goal.popleft()
result = []

while cur_num < n + 1 and stk: 
    stk.append(cur_num)
    result.append('+')
    if stk[-1] == cur_match:
        while stk[-1] == cur_match:
            try:
                cur_match = goal.popleft()
            except:
                pass
            stk.pop()
            result.append('-')
        cur_num += 1
        continue
    if stk[-1] > cur_match:
        break
    cur_num += 1

if len(result) < 2 * n - 1:
    print('NO')
else:
    print('\n'.join(result))