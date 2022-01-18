import sys
input = sys.stdin.readline
MAX = 9876543210
def solve():
    R,C = map(int,input().split())
    
    board = [0] * R
    for i in range(R):
        board[i] = list(input().rstrip())
    
    cache = [[0] * C for i in range(R)]
    SEARCH_RANGES = [[1,0], [0,1], [-1,0], [0,-1]]

    def wrong_range(new_r,new_c):
        if new_r < 0 or new_r > R-1 or new_c < 0 or new_c > C-1:
            return 1
        return 0
    def find_bird():
        result = (-1,-1)
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'L':
                    result = r,c
        return result

    visited = [[0] * C for i in range(R)]
    start_r, start_c = find_bird()
    board[start_r][start_c] = '.'
    nxt_findings = [(0, start_r, start_c)]
    while nxt_findings:
        findings = nxt_findings
        nxt_findings = []
        while findings:
            print(findings)
            cur_cost, r,c = findings.pop()
            if visited[r][c]:
                continue
            if board[r][c] == 'L':
                break
            visited[r][c] = 1
            
            for r_p, c_p in SEARCH_RANGES:
                new_r = r+r_p
                new_c = c+c_p
                if wrong_range(new_r,new_c)or visited[new_r][new_c]:
                    continue
                if board[new_r][new_c] == 'X':
                    nxt_findings.append((cur_cost + 1, new_r,new_c))
                else:
                    findings.append((cur_cost,new_r,new_c))
            
    print(cur_cost)
solve()