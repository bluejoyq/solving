def solve():
    import sys
    input = sys.stdin.readline
    N,M,K = map(int,input().split())


    def is_valid(r,c):
        if -1 < r < N and -1 < c <M:
            return True
        return False
    board = []
    cache = []
    board_cache = [[0] * M for i in range(N)]
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(M):
            if row[j] == 1:
                cache.append((i,j))
        board.append(row)

    plant_count = len(cache)
    if plant_count == K:
        print(plant_count)
        for r,c in cache:
            print(r + 1, c + 1)
        return
    elif plant_count == 2 * K:
        print(0)
        return

    elif plant_count == 2 * K - 1:
        r,c = cache[0]
        r2,c2 = cache[1]
        r_plus = r2 - r
        c_plus = c2 - c

        for i in range(K-1):
            check_r = r + c_plus
            check_c = c + r_plus
            if is_valid(check_r, check_c) and board[check_r][check_c]:
                print(1)
                print(r + 1 , c + 1)
                return
            check_r = r - c_plus
            check_c = c - r_plus
            if is_valid(check_r, check_c) and board[check_r][check_c]:
                print(1)
                print(r + 1 , c + 1)
                return
            r += r_plus
            c += c_plus

    counting = 2 * K -plant_count
    print(counting)
    for i in range(counting):
        r,c =cache[i + K - counting]
        print(r + 1 , c+ 1)
solve()