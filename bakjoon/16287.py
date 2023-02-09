
def solve():
    from itertools import combinations
    W,N = map(int,input().split())

    values = list(map(int,input().split()))
    cache = [0] * 800000

    for i in range(3, N-1):
        for a in combinations(values[:i],2):
            sum_num = sum(a)
            cache[sum_num] = 1
            for b in combinations(values[i:],2):
                sum_b = sum(b)
                if sum_b >= W:
                    continue
                if cache[W-  sum_b]:
                    return 'YES'
    return 'NO'
print(solve())