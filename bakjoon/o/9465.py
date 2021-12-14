import sys
input = sys.stdin.readline
T = int(input())

def solve():
	N = int(input())
	values = [0,0]
	for i in range(2):
		values[i] = list(map(int, input().split()))

	cache = [[0] * (N + 2) for i in range(2)]
	
	for r in range(N):
		for c in range(2):
			cur = cache[c][r]
			cache[1 - c][r + 1] = max(cache[1 - c][r + 1], cur + values[c][r])
			cache[1 -c][r + 2] = max(cache[1 -c][r + 2], cur + values[c][r])
	print(max(cache[0][N+1], cache[1][N+1]))
for _ in range(T):
	solve()