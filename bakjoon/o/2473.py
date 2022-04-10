def solve():
    N = int(input())
    values = list(map(int,input().split()))
    values.sort()
    min_goal = 1204120412041240
    min_goals = []
    for cur in values:
        left = 0
        right = N - 1

        while left < right:
            if values[left] == cur:
                left += 1
                continue
            if values[right] == cur:
                right -= 1
                continue
            cur_goal = values[left] + values[right] + cur
            if cur_goal == 0:
                min_goals = [values[left], values[right],cur]
                return min_goals
            elif min_goal > abs(cur_goal):
                min_goal = abs(cur_goal)
                min_goals = [values[left], values[right],cur]
            
            if cur_goal > 0:
                right -= 1
            else:
                left += 1
    return min_goals

result = solve()
print(*sorted(result))