def solution(info, edges):
    N = len(info)
    node = [[0] * N for i in range(N)]
    for edge in edges:
        node[edge[0]][edge[1]] = 1
    
    answer = 0
    # cur, sheep, wolf, visited

    findings = [(0,1,0,[0 for i in range(N)])]
    while findings:
        cur,s_count,w_count,can_go = findings.pop()
        answer = max(s_count, answer)
        for nxt in range(N):
            if node[cur][nxt] == 0:
                continue
            can_go[nxt] = 1
        for nxt in range(N):
            if can_go[nxt] == 0 or (info[nxt] == 1 and s_count - w_count == 1):
                continue
                
            new_can_go = can_go[:]
            new_can_go[nxt] = 0
            if info[nxt] == 0:
                findings.append((nxt,s_count + 1,w_count, new_can_go))
            else:
                findings.append((nxt,s_count,w_count + 1, new_can_go))
    return answer