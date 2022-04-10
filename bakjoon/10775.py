import sys
input = sys.stdin.readline
G = int(input())
P = int(input())

gates_count = G
for i in range(P):
    g = int(input())
    if gates_count < g:
        break
    gates_count -= 1
print(i)