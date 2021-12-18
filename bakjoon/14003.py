import sys
from bisect import bisect_left
input = sys.stdin.readline
MAX = 98765432100
N = int(input())
values = list(map(int,input().split()))

cache = [MAX] *(N + 2)
idx_cache = [0] * (N+2)
pos_cache = [0] * (N)
max_pos = 0
for idx in range(N):
	value = values[idx]
	if cache[max_pos] < value:
		max_pos += 1
		pos = max_pos
	else:
		pos = bisect_left(cache, value, hi = max_pos+1)
	pos_cache[idx] = pos
	cache[pos] = value
	idx_cache[pos] = idx

last_pos = cache.index(MAX)
print(last_pos)

cur_pos = last_pos - 1
cur_idx = idx_cache[cur_pos]
#print(idx_cache)
#print(cache)
#print(pos_cache)
loop_count = 0
for cur_pos in range(last_pos - 1, -1, -1):
	bef_idx = idx_cache[cur_pos - 1]
	if bef_idx < cur_idx:
		cur_idx = bef_idx
		continue
	for idx in range(cur_idx - 1, -1,-1):
		loop_count+= 1
		#if values[idx] >= values[idx_cache[cur_pos]]:
		#		continue
		if pos_cache[idx] != cur_pos - 1:
			continue
		cache[cur_pos - 1] = values[idx]
		cur_idx = idx
		break

print(loop_count)
print(*cache[:last_pos])