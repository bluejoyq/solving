from heapq import heappush, heappop
N = int(input())
values = [0] * N

for i in range(N):
    values[i] = int(input())

que = []
for i in range(N - 1):
    heappush(que, (values[i] + values[i + 1], i, i+1))

visited = [0] * N
lefts = [i -1 for i in range(N)]
rights = [i + 1 for i in range(N)]

while que:
    cur_val, left, right = heappop(que)
    
    if left == 0 and right == N-1:
        print(cur_val)
        break
    
    if left > 0 and lefts[left - 1] > -1:
        heappush(que, (cur_val * 2+ values[lefts[left - 1]]))
    if right < N - 1 and rights[right +  1] < N:
        heappush(que, (cur_val * 2+ values[rights[right +  1]]))
    lefts[right] = left
    rights[left] = right