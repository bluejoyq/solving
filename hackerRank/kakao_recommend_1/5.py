def solution(tree_nodes, tree_from, tree_to):
    from collections import deque
    edges = [{} for i in range(tree_nodes)]
    
    for i in range(tree_nodes - 1):
        edges[tree_to[i] - 1][tree_from[i] - 1] = 1
        edges[tree_from[i] - 1][tree_to[i] - 1] = 1
    
    def bfs(start):
        visited = [0] * tree_nodes
        findings = deque([(start,0)])
        last_cost = 0
        last_values = []
        while findings:
            cur,cost = findings.popleft()
            if cost > last_cost:
                last_cost = cost
                last_values = []
                
            visited[cur] = 1
            last_values.append(cur)
            
            for nxt in edges[cur].keys():
                if visited[nxt]:
                    continue
                visited[nxt]= 1
                findings.append((nxt, cost + 1))
        
        return last_values
    
    a_dias = bfs(0)
    b_dias = bfs(a_dias[0])
    
    result = [0] * tree_nodes
    for a in a_dias:
        result[a] = 1
    for b in b_dias:
        result[b] = 1
    return result