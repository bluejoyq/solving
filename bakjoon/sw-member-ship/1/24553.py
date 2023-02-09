import sys
input = sys.stdin.readline
def is_p(num):
    str_num = str(num)
    for i in range(len(str_num) // 2):
        if str_num[i] != str_num[-i - 1]:
            return False
    return True
def solve():
    N = int(input())
    while True:
        for j in range(N, -1, -1):
            if not is_p(j):
                continue
            print("d",j)
            N -= j
            break
        if N == 0:
            return i % 2



T = int(input())
for i in range(T):
    print(solve())