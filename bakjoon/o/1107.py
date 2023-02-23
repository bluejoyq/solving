
def list_to_int(values):
    result = 0
    for i in range(1, len(values) + 1):
        result += values[-i] * 10 ** (i - 1)
    return result
def solve(N,M, wrong_buttons):
    from itertools import product
    MAX = 999999
    cache = [MAX] * MAX

    buttons = set([i for i in range(10)])
    
    for btn in wrong_buttons:
        buttons.remove(btn)


    for i in range(1, 7):
        for val in product(buttons,repeat= i):
            cur_pos = list_to_int(val)
            if cur_pos > MAX - 1:
                continue
            cache[cur_pos] = min(cache[cur_pos], len(val))

    cache[100] = 0
    pos = 0
    result = MAX
    for i in range(MAX):
        result = min(result , cache[i] + abs(N - i))
    return result


N = int(input())
M = int(input())
wrong_buttons = []
if M > 0:
    wrong_buttons += list(map(int, input().split()))
print(solve(N,M,wrong_buttons))

# assert solve(5457, 3 ,[6,7,8]) == 6
# assert solve(100,5,[0,1,2,3,4]) == 0
# assert solve(500000, 8, [0,2,3,4,6,7,8,9]) == 11117

# assert solve(100, 3, [1,0,5]) == 0

# assert solve(14124, 0 , []) == 5


# assert solve(1,9,[1,2,3,4,5,6,7,8,9]) == 2
# assert solve(80000,2,[8,9]) == 2228