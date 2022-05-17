import sys
input = sys.stdin.readline


def solve():

    def is_valid(r, c):
        if r > N-1 or r < 0 or c > N-1 or c < 0:
            return False
        return True

    def original_checker(cur_r, cur_c, nxt_r, nxt_c):
        if values[cur_r][cur_c] == values[nxt_r][nxt_c]:
            return True
        return False

    def color_blind_checker(cur_r, cur_c, nxt_r, nxt_c):
        if values[cur_r][cur_c] == values[nxt_r][nxt_c]:
            return True
        if values[cur_r][cur_c] == 'G' and values[nxt_r][nxt_c] == 'R':
            return True
        if values[cur_r][cur_c] == 'R' and values[nxt_r][nxt_c] == 'G':
            return True
        return False

    def dfs(r, c, checker):
        findings = [(r, c)]
        while findings:
            cur_r, cur_c = findings.pop()
            visited[cur_r][cur_c] = 1
            for r_plus, c_plus in nxt_moves:
                nxt_r = cur_r + r_plus
                nxt_c = cur_c + c_plus
                if not is_valid(nxt_r, nxt_c):
                    continue
                if visited[nxt_r][nxt_c] or not checker(cur_r, cur_c, nxt_r, nxt_c):
                    continue
                visited[nxt_r][nxt_c] = 1
                findings.append((nxt_r, nxt_c))
    N = int(input())

    nxt_moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    values = [list(input()) for i in range(N)]

    visited = [[0] * N for i in range(N)]
    real_count = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
            real_count += 1
            dfs(r, c, original_checker)
    visited = [[0] * N for i in range(N)]
    color_blind_count = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
            color_blind_count += 1
            dfs(r, c, color_blind_checker)
    print(real_count, color_blind_count)


solve()
