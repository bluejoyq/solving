N = int(input())
values = list(map(int,input().split()))

left = 0
right = N-1
best_std = 9876543210000
best_idx = [-1,-1]
while left < right:
    std = values[left] + values[right]
    if abs(std) < best_std:
        best_std = abs(std)
        best_idx = [left, right]
    if std == 0:
        break
    if std < 0:
        left += 1
    elif std > 0:
        right -= 1
print(values[best_idx[0]], values[best_idx[1]])
    
