import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    values = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        orders = list(map(int, input().split()))
        cmd = orders[0]
        if cmd == 1:
            
