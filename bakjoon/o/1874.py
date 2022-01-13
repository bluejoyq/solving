import sys
input = sys.stdin.readline
n = int(input())
stk =[0]
cur_num = 1
result = []
for i in range(n):
    cur_match_goal = int(input())

    while stk[-1] < cur_match_goal:
        stk.append(cur_num)
        result.append('+')
        cur_num += 1

    if stk[-1] > cur_match_goal:
        break
    stk.pop()
    result.append('-')

if len(result) < 2 * n - 1:
    print('NO')
else:
    print('\n'.join(result))