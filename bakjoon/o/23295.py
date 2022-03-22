import sys
input = sys.stdin.readline
MAX = 100005
N,T = map(int, input().split())
plus_times = [0] * MAX
end_times = [0] * MAX
for i in range(N):
    K = int(input())
    for j in range(K):
        a,b = map(int, input().split())
        plus_times[a] += 1
        end_times[b] += 1

last_plus = [0] * MAX
cur_time_sum = 0
cur_plus = 0 
for i in range(T):
    cur_plus += plus_times[i]
    cur_plus -= end_times[i]
    cur_time_sum += cur_plus
    last_plus[i] = cur_plus

max_time = cur_time_sum
max_time_end = T
for i in range(T, MAX):
    cur_plus += plus_times[i]
    cur_plus -= end_times[i]
    cur_time_sum += cur_plus
    cur_time_sum -= last_plus[i - T]
    last_plus[i] = cur_plus
    if max_time < cur_time_sum:
        max_time =cur_time_sum
        max_time_end = i + 1

print(max_time_end - T, max_time_end)