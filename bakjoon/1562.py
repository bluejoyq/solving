N = int(input())


def solve(N):
    cache = [[0] * 10 for i in range(N)]

    
    cache[9][0] = 1
        
    for pos in range(10, N):
        
        cache[pos][0] += cache[pos - 1][1]
        for num in range(1,9):
            cache[pos][num] += cache[pos - 1][num - 1]
            cache[pos][num] += cache[pos - 1][num + 1]
        cache[pos][9] += cache[pos - 1][8]
    return(sum(cache[N-1])) , cache

tmp, cache = solve(40)

print(sum([sum(c) for c in cache]))


