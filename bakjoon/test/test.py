import sys
input = sys.stdin.readline

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


N = int(input())
card_list = list(map(int, input().split()))
M = int(input())
check_list = list(map(int, input().split()))

card_list.sort()
for check_num in check_list:
    count = 0
    while True:
        result = binary_search(card_list, check_num, 0, len(card_list) - 1)
        if result is None:
            break
        else:
            card_list.pop(result)
            count += 1
    print(count, end=' ')