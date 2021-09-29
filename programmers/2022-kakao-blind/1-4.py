def solution(n, info):
    M = 11
    cache= [[-1] *(n + 1) for i in range(M) ]
    # cache[M][n]
    for i in range(M):
        need = info[i] + 1
        if need <= n:
            cache[i][need] = 10 - i
        for j in range(n+1):
            if cache[i - 1][j] == -1:
                continue
            try:
                cache[i][j + need] = cache[i - 1][j] + 10 - i
            except:
                pass
    print(cache)
    answer = []
    return answer
solution(5,	[2,1,1,1,0,0,0,0,0,0,0])