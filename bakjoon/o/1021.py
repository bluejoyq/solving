from collections import deque
N, M = map(int, input().split())
targets = list(map(int, input().split()))

def right_rotate(que):
    que.appendleft(que.pop())

def left_rotate(que):
    que.append(que.popleft())

que = deque([i for i in range(1, N+1)])
result = 0

for target in targets:
    que_lenght = len(que)
    idx = que.index(target)
    if idx > que_lenght // 2:
        rotate_func = right_rotate
        rotate_num = que_lenght - idx

    else:
        rotate_func = left_rotate
        rotate_num =idx

    result += rotate_num
    for i in range(rotate_num):
        rotate_func(que)

    que.popleft()
print(result)
