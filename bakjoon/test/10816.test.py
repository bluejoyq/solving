import sys
input = sys.stdin.readline
def solve_wrong(card_list, check_list):
    def binary_search(array, target, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binary_search(array, target, start, mid - 1)
        else:
            return binary_search(array, target, mid + 1, end)


    N = len(card_list)
    M = len(check_list)

    card_list.sort()
    tmp = []
    for check_num in check_list:
        count = 0
        while True:
            result = binary_search(card_list, check_num, 0, len(card_list) - 1)
            if result is None:
                break
            else:
                card_list.pop(result)
                count += 1
        tmp.append(count)
    return tmp


import sys
input = sys.stdin.readline
def solve(values, targets):
    values_count = [0] * 20000000
    for value in values:
        values_count[value] += 1
    result = []

    for target in targets:
        result.append(values_count[target])
    return result


import random

while True:
    N = 10
    values = [random.randint(-10,10) for i in range(N)]
    M = 5
    targets = [random.randint(-11,11) for i in range(M)]

    a = solve(values,targets)
    b = solve_wrong(values,targets)
    print(values,targets)
    print(a,b)
    if a == b:
        continue
    break
print(N)
print(*values)
print(M)
print(*targets)
print(a,b)