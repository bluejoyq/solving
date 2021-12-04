def solution(arr, x):
    N = 10**9 + 1
    x_checker = [0] * x
    for num in arr:
        x_checker[num % x] += 1
    for i in range(N):
        if x_checker[i % x] == 0:
            return i
        x_checker[i % x] -= 1
