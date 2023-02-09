import sys
input = sys.stdin.readline
def power(a,k,mod):
    res = 1
    while k > 0:
        if k % 2 != 0:
            res = (res * a) % mod
        k //= 2
        a = (a ** 2) % mod
    return res

def miller(x,a):
    r = 0
    d = x-1
    while d%2 == 0:
        r += 1
        d = d // 2
    xx = power(a,d,x)
    if xx == 1 or xx == x-1:
        return 1
    for _ in range(0,r-1):
        xx = power(xx,2,x)
        if xx == x-1:
            return 1
    return 0

def is_prime(x):
    for a in a_list:
        if not miller(x,a):
            return 0
    return 1
a_list = [2,3,5,7,13,17]
n = int(input())
result = 0
for i in range(n):
    x = int(input())
    result += is_prime( 2* x + 1)
print(result)