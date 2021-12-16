import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
root = {}
for i in range(N):
	values = list(input().split())
	cur = root
	for value in values[1:]:
		try:
			cur = cur[value]
		except:
			cur[value] = {}
			cur = cur[value]

cur = root
def dfs(cur, depth):
	for nxt in sorted(cur.keys()):
		print('--' * depth + nxt + '\n')
		dfs(cur[nxt], depth + 1)
dfs(root, 0)
