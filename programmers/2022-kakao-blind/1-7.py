def solution(board, aloc, bloc):
    # 모든 경우에서 생존의 수가없으면 종료. => nxt_findings 가 없으면.
    N = len(board)
    M = len(board[0])
    search_range = [[0,1],[1,0],[0,-1],[-1,0]]
    findings = [(aloc, bloc, [[0 for i in range(M)] for i in range(N)])]
    answer = 0
    for i in range(30):
        nxt_findings = []
        while findings:
            a,b,removed = findings.pop()
            removed[a[0]][a[1]] = 1
            removed[b[0]][b[1]] = 1
            for plus_r,plus_c in search_range:
                a_r = a[0] + plus_r
                a_c =  a[1] + plus_c
                if -1 < a_r < N and -1 < a_c < M and board[a_r][a_c] == 1 and removed[a_r][a_c] == 0:
                    for plus_rr,plus_cc in search_range:
                        b_r = b[0] + plus_rr
                        b_c = b[1] + plus_cc
                        if -1 < b_r < N and -1 < b_c < M and board[b_r][b_c] == 1 and removed[b_r][b_c] == 0:
                            nxt_findings.append(([a_r,a_c],[b_r,b_c], [r[:]for r in removed]))
        findings = nxt_findings
    
    return i
solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]],	[1, 0],	[1, 2])