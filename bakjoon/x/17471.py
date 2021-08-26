# https://www.acmicpc.net/problem/17471


# N이 최대 10이므로 2^10 = 1024 모든 경우를 다해봐도 된다.
def solve():
    N = int(input())
    values = list(map(int, input().split()))
    bit_range = pow(2,N)
    for bit_idx in range(1, bit_range):
        pass