from heapq import heappop, heappush

N,M = map(int, input().split())
visited = [0] * 110
edges = [0] * 110
for i in range(N + M):
    x,y = map(int, input().split())
    edges[x]= y


findings = [(0,1)]
while findings:
    cur_val,cur_pos = heappop(findings)
    
    
    if cur_pos == 100:
        print(cur_val)
        break
    elif cur_pos > 100:
        continue
    if visited[cur_pos]:
        continue
    visited[cur_pos] = 1
    for move in range(1, 7):
        nxt_pos = cur_pos + move
        if visited[nxt_pos]:
            continue
        if edges[nxt_pos]:
            nxt_pos = edges[nxt_pos]
        heappush(findings,(cur_val + 1,nxt_pos) )
        
