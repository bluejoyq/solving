import sys
from itertools import combinations
def gcd(a, b):
    while (b != 0):
        temp = a % b
        a = b
        b = temp
    return abs(a)
def lcm(a, b):
    gcd_value = gcd(a, b)
    if (gcd_value == 0): 
        return 0
    return abs( (a * b) / gcd_value )
input = sys.stdin.readline

def solve():
    N = int(input())
    tmp = []
    result = 0
    str_num = "11"
    while N >= int(str_num):
        num = int(str_num)
        tmp.append(num)
        result += N // num
        str_num += "1"
    for i in range(2,len(tmp) +  1):
        for t in combinations(tmp, i):
            val = (-1) ** i
            l = 1
            for val in t:
                l = lcm(val, l)
            result -= N // l
    return result
print(solve())